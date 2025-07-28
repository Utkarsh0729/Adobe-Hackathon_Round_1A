import fitz
import os
import json
from langdetect import detect

def extract_headings_from_pdf(pdf_path):
    CONFIG = {
        "MIN_FONT_SIZE": 14.0,
        "H1_FONT_SIZE": 16.0,
        "MIN_TEXT_LENGTH": 2,
        "TITLE_PAGE_NUM": 0
    }

    doc = fitz.open(pdf_path)
    outline = []
    combined_title = []
    text_snippets = []

    toc = doc.get_toc()
    if toc:
        for level, text, page_num in toc:
            outline.append({
                "level": f"H{level}",
                "text": text,
                "page": page_num - 1
            })
        if outline:
            combined_title.append(outline[0]['text'])

    if not toc:
        for page_num in range(len(doc)):
            page = doc[page_num]
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        spans = line["spans"]
                        if not spans:
                            continue
                        
                        text = " ".join(span["text"].strip() for span in spans).strip()

                        if not text or len(text) < CONFIG["MIN_TEXT_LENGTH"]:
                            continue

                        if len(text_snippets) < 10:
                            text_snippets.append(text)

                        font_size = spans[0]["size"]
                        font_flags = spans[0]["flags"]
                        is_bold = font_flags & 2 != 0

                        if font_size > CONFIG["MIN_FONT_SIZE"] or is_bold:
                            level = "H1" if font_size >= CONFIG["H1_FONT_SIZE"] else "H2"
                            heading = {
                                "level": level,
                                "text": text,
                                "page": page_num
                            }
                            outline.append(heading)
                            
                            if page_num == CONFIG["TITLE_PAGE_NUM"] and level == "H1":
                                combined_title.append(text)
    
    if not text_snippets:
        try:
            first_page = doc.load_page(0)
            text_for_lang = first_page.get_text()
            language = detect(text_for_lang) if text_for_lang else "unknown"
        except:
            language = "unknown"
    else:
        language = detect(" ".join(text_snippets)) if text_snippets else "unknown"

    doc.close()

    return {
        "title": " ".join(combined_title).strip() or "Unknown Title",
        "language": language,
        "outline": outline
    }

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' not found. Please create it and add PDF files.")
        return

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            
            try:
                print(f"Processing '{filename}'...")
                result = extract_headings_from_pdf(pdf_path)

                output_filename = f"output_{os.path.splitext(filename)[0]}.json"
                output_path = os.path.join(output_dir, output_filename)

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=4)
                
                print(f"-> Successfully generated '{output_filename}'.")

            except Exception as e:
                print(f"!! Could not process '{filename}'. Reason: {e}")

if __name__ == "__main__":
    main()