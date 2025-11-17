# QR Code Generator

A simple Django app that generates QR codes from text or URLs. It works both as a website with a clean interface and as an API for developers.

## What It Does

- Type any text or URL and get a QR code instantly
- Download the QR code as PNG image
- Use the same functionality via API
- No signup or login required

## For Website Users

Just visit the homepage, type your text, and the QR code appears automatically. Click "Download" to save it.

## For Developers (API)

**Base URL:** `https://.onrender.com`

**Generate QR Code:**

GET /apiEnd/?text=YourTextHere

**Example using curl:**
```bash
curl "https://your-app.onrender.com/apiEnd/?text=Hello%20World"

Successful Response:

{
    "status": 200,
    "img_url": "base64_encoded_string_here",
    "data": "Your original text"
}

Error Response:

{
    "status": 400,
    "failer": "no data found"
}

The img_url contains a base64 encoded PNG image that you can decode and save as a file.

Running Locally

1. Clone the repo

2. Install requirements: pip install -r requirements.txt

3. Run: python manage.py runserver

4. Open http://localhost:8000

Technology

- Django (Backend)

- qrcode library (QR generation)

- Tailwind CSS (Frontend styling)

- Vanilla JavaScript (Frontend logic)

- Render (Hosting)

Project Structure

The app uses a single Django view that handles both web and API requests, returning JSON for API calls and rendering templates for web users.