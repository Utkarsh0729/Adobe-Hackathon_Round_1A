# PDF Heading Extractor

## 📖 Description

This project is a **Python script** that extracts headings, titles, and language from PDF files. It processes each PDF in a specified `input` directory and, for each file, it generates a **JSON file** containing the extracted information. The entire process is containerized using **Docker**, making it easy to run in a consistent and isolated environment.

---

## 📂 Project Structure

Here is the file and directory structure for this project:

.
├── input/
│   └── (Your PDF files go here)
├── output/
│   └── (Generated JSON files will be saved here)
├── main.py
└── Dockerfile


* **`input/`**: This directory is where you should place all the PDF files that you want to process.
* **`output/`**: After processing, the script will save the resulting JSON files in this directory.
* **`main.py`**: The main Python script that contains all the logic for extracting information from the PDFs.
* **`Dockerfile`**: A text file that contains all the commands, in order, needed to build the Docker image for this project.

---

## 🏛️ Architecture

This project is designed with a straightforward and efficient architecture, which can be broken down into two main components:

1.  **Python Script (`main.py`)**:
    * **File Handling**: The script is designed to read PDF files from a designated `input` directory and write the output to a corresponding `output` directory.
    * **PDF Processing**: It uses the **`PyMuPDF`** library to open and parse PDF files, extracting text blocks and their properties, such as font size and style.
    * **Heading Detection**: Headings are identified based on font size and whether the text is bold. This allows the script to create a structured outline of the document.
    * **Language Detection**: The **`langdetect`** library is used to determine the language of the text in the PDF.
    * **JSON Output**: The extracted information, including the title, language, and a detailed outline, is saved in a well-structured JSON format.

2.  **Docker Environment**:
    * **Base Image**: The project uses a lightweight **`python:3.11-slim`** base image to keep the overall size of the Docker image small.
    * **Dependencies**: The `Dockerfile` handles the installation of all necessary system libraries (like `libmupdf-dev`) and Python packages (such as `PyMuPDF` and `langdetect`).
    * **Containerization**: By containerizing the application, we ensure that it runs in a consistent environment, regardless of the host system. This eliminates the "it works on my machine" problem.
    * **Automation**: The `CMD` instruction in the `Dockerfile` specifies the command to run when the container starts, automating the execution of the Python script.

---

## 🐳 Docker Commands

To build and run this project using Docker, follow these simple steps.

### 1. Build the Docker Image

First, you need to build the Docker image from the `Dockerfile`. Open your terminal or command prompt, navigate to the project's root directory (where the `Dockerfile` is located), and run the following command:

```bash
docker build -t pdf-extractor .
docker build: The command to build a Docker image.
```

2. Run the Docker Container
Once the image is built, you can run it as a container. This command will also mount the input and output directories from your local machine to the container, allowing the script to access your PDF files and save the JSON output back to your machine.

```
docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" pdf-extractor
docker run: The command to run a Docker container.
```

pdf-extractor: The name of the image to run.

After running this command, the script will start processing the PDFs in your input folder, and you will see the JSON files appear in your output folder.
