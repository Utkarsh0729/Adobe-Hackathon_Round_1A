# Adobe Hackathon PDF Extractor

This project is a Python script that extracts structured information from PDF files, such as headings, titles, and language, and saves the output as a JSON file.

***

## How it Works

The script processes PDF files to identify and extract key textual elements. It uses two primary methods for this:

1.  *Table of Contents (TOC):* If a PDF has a built-in Table of Contents, the script will use it to get the primary headings and the document's title.
2.  *Font Analysis:* If no TOC is available, the script analyzes the text on each page. It identifies headings by looking for text with a font size larger than a predefined minimum (14.0) or text that is bold. It distinguishes between H1 and H2 level headings based on font size (H1 >= 16.0).

The script also detects the primary language of the document by analyzing the initial text snippets.

***

## Features

* *Title Extraction:* Automatically extracts the document's title.
* *Heading Extraction:* Identifies and lists all headings (H1 and H2) along with their corresponding page numbers.
* *Language Detection:* Determines the language of the document's text.
* *JSON Output:* Saves the extracted data in a structured and easy-to-read JSON file.

***

## Dependencies

The solution relies on the following Python libraries:

* **PyMuPDF (fitz):** For opening, reading, and extracting content from PDF files.
* *langdetect:* To detect the language of the text.

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
How to Use
Create Directories:

Create an input folder and place all the PDF files you want to process into this directory.

The script will automatically create an output folder to store the results.

Run the Script:
Execute the main.py script from your terminal:

python main.py

Get the Output:

For each processed PDF, a corresponding JSON file will be generated in the output directory. For example, a PDF named mydocument.pdf will produce output_mydocument.json.

The terminal will show the progress and indicate whether each file was processed successfully.

Output Format
The output for each PDF is a JSON file containing the document's title, its detected language, and a detailed outline of its headings.

Example output.json:

{
    "title": "Example Document Title",
    "language": "en",
    "outline": [
        {
            "level": "H1",
            "text": "Main Section 1",
            "page": 0
        },
        {
            "level": "H2",
            "text": "Subsection 1.1",
            "page": 1
        }
    ]
}   