import pytesseract
from PIL import Image
import os

def extract_and_append_text(image_path, label):
    if not os.path.isfile(image_path):
        print(f"[OCR] File not found: {image_path}")
        return

    try:
        # Extract text from image
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img).strip()

        # Determine base folder and filenames
        folder = os.path.dirname(image_path)
        top_folder_name = os.path.basename(folder)
        base_name = os.path.basename(image_path)

        txt_path = os.path.join(folder, f"{top_folder_name}-extracted.txt")
        html_path = os.path.join(folder, f"{top_folder_name}-extracted.html")

        # Format for .txt file
        txt_entry = f"[{label}] {base_name}\n{text}\n" + "-" * 40 + "\n"

        # Format for HTML
        html_entry = f"""
        <div class="entry {label.lower()}">
          <h4>[{label}] {base_name}</h4>
          <pre>{text}</pre>
        </div>
        """

        # Append to text file
        with open(txt_path, "a", encoding="utf-8") as f:
            f.write(txt_entry)

        # Append or create HTML file
        if not os.path.exists(html_path):
            with open(html_path, "w", encoding="utf-8") as f:
                f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Extracted Text</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    .entry { border-bottom: 1px solid #ccc; margin-bottom: 20px; padding-bottom: 10px; }
    .q { background-color: #e6f0ff; }
    .a { background-color: #e9ffe6; }
    h4 { margin-bottom: 5px; }
    pre { white-space: pre-wrap; word-wrap: break-word; }
  </style>
</head>
<body>
  <h2>Extracted Text</h2>
""")

        with open(html_path, "a", encoding="utf-8") as f:
            f.write(html_entry)

        print(f"[OCR] Saved to:\n - {txt_path}\n - {html_path}")

    except Exception as e:
        print(f"[OCR] Error extracting text: {e}")
