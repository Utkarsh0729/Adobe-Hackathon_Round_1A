FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install --no-install-recommends -y libmupdf-dev build-essential && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir PyMuPDF langdetect
COPY extract_headings.py .
RUN mkdir input output
CMD ["python", "extract_headings.py"]
