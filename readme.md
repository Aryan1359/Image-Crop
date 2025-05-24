
# 🖼️ Image Crop & OCR App (Django + Anaconda + Bootstrap)

This project is a Django web app that allows you to:

- View images from a selected folder
- Crop images with mouse (manual selection)
- Label cropped images as "Q" (question) or "A" (answer)
- Automatically extract text using Tesseract OCR
- Save the text to `.txt` and `.html` files

---

## 🛠️ Setup Instructions (Anaconda + Windows)

### 1. Clone the Project

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd Image-Crop
```
````

### 2. Create and Activate Virtual Environment

```bash
conda create -n imagecrop_env python=3.11
conda activate imagecrop_env
```

### 3. Install Requirements

```bash
pip install django pillow pytesseract cropperjs
```

> ✅ Make sure you have [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki) installed and added to system PATH.

Test in terminal:

```bash
tesseract --version
```

### 4. Run Initial Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Features

- Keyboard shortcuts:

  - ← / → to navigate images
  - `C` to crop
  - `Delete` to delete

- Cropped images saved as `Q_*.jpg` or `A_*.jpg`
- OCR results saved in:

  - `FOLDERNAME-extracted.txt`
  - `FOLDERNAME-extracted.html` (color-coded)

---

## 📁 Folder Structure

```
Image-Crop/
├── extractor/         # OCR app
├── viewer/            # Image display + crop logic
├── templates/         # HTML files
├── media/             # Temp cropped image storage
├── manage.py
├── README.md
└── requirements.txt   # (Optional if used)
```

---

## 🔁 Common Commands

```bash
# Start Django dev server
python manage.py runserver

# Apply model changes
python manage.py makemigrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser
```

---

## 🤖 OCR Output Sample (HTML)

```html
<div class="entry q">
  <h4>[Q] Q_example.jpg</h4>
  <pre>What is 2 + 2?</pre>
</div>
<div class="entry a">
  <h4>[A] A_example.jpg</h4>
  <pre>4</pre>
</div>
```

---

## 🔒 Notes

- This app works **offline** — no image data is sent to any server.
- You can safely delete `media_temp/` after closing the app.

---

```

Let me know if you'd like to change the formatting, add screenshots, or make this multilingual.

---

## ✅ Step 2: Initialize Git & Push to GitHub

I'll walk you through it next.

Would you like me to:
1. Show the exact Git commands to run in Anaconda?
2. Or help you first create a new private GitHub repo?

Let me know and we’ll push it cleanly next.
```
