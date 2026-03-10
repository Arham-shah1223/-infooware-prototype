import argparse

from modules.extract_text import extract_text
from modules.summarize import summarize_text
from modules.create_slides import create_slides
from modules.create_video import create_video


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)

    args = parser.parse_args()

    pdf_path = args.input
    outdir = args.outdir

    print("Extracting text...")
    text = extract_text(pdf_path)

    print("Summarizing...")
    points = summarize_text(text)

    print("Creating slides...")
    slides_path = outdir + "/slides.pptx"
    create_slides(points, slides_path)

    print("Slides created:", slides_path)

    print("Creating video...")
    video_path = outdir + "/video.mp4"
    create_video(slides_path, video_path)

    print("Video created:", video_path)


if __name__ == "__main__":
    main()