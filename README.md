# Infooware Edu Prototype — PDF to Slides & Video

## Project Overview
This project converts a PDF document into:
1. A visual slide deck (PowerPoint)
2. A short animated explainer video

The system extracts key points from a PDF and automatically generates slides and a short video explanation.

---

## Technologies Used

- Python
- pdfplumber
- python-pptx
- moviepy
- pillow
- pyttsx3
- nltk

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

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python run_pipeline.py --input input/sample.pdf --outdir output

---

## Output

The program generates:

- slides.pptx → Visual slide presentation
- video.mp4 → Short animated video from slides

---

## Example Use Case

This prototype can be used for:

- Educational content generation
- Automated lecture summarization
- Quick learning material creation
