# Infooware Edu Prototype – PDF to Slides & Video

## Project Overview
This project converts a PDF document into:
1. A short slide deck explaining key concepts.
2. A short video generated from the slides.

Pipeline:
PDF → Text Extraction → Summarization → Slides → Video

---

## Tech Stack

- Python
- pdfplumber
- python-pptx
- moviepy
- pillow

---

## Project Structure

infooware-prototype
│
├── input
│   └── sample.pdf
│
├── modules
│   ├── extract_text.py
│   ├── summarize.py
│   ├── create_slides.py
│   └── create_video.py
│
├── output
│   ├── slides.pptx
│   └── video.mp4
│
├── run_pipeline.py
├── requirements.txt
└── README.md


---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Run the Project

Run the pipeline using:

python run_pipeline.py --input input/sample.pdf --outdir output

---

## Output

The pipeline generates:

slides.pptx → PowerPoint slides summarizing the PDF

video.mp4 → Short video created from the slides

---

## Example

Input:

input/sample.pdf

Output:

output/slides.pptx

output/video.mp4

---

## Author

Arham Shah