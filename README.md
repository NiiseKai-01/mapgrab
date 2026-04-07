# MapGrab

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask&logoColor=white)
![SerpAPI](https://img.shields.io/badge/SerpAPI-Google_Maps-4285F4?logo=googlemaps&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

MapGrab is a web-based Google Maps lead scraper. Enter a search query — such as a business type and location — and MapGrab fetches up to 100 results from Google Maps via SerpAPI, then exports the data as a downloadable CSV and Excel file.

---

## Features

- Scrapes up to 100 Google Maps listings per query across paginated results
- Extracts business name, address, phone number, rating, review count, price, type, operating hours, Google Maps link, and GPS coordinates
- Exports results to both CSV and Excel (.xlsx) formats
- Excel output includes clickable hyperlinks in the Google Maps Link column
- Demo mode available using the query `demoliveshowcase` — no API key required
- Old generated files are automatically cleaned up before each new export

---

## Project Structure

```
mapgrab/
├── scrapper.py              # Flask app entry point
├── routes.py                # API route definitions
├── requirements.txt         # Python dependencies
├── procfile                 # Gunicorn process config (for deployment)
├── sample.json              # Sample data used for demo mode
├── files/                   # Generated CSV and Excel output files
├── templates/
│   └── index.html           # Frontend UI
└── services/
    ├── jsfetcher.py         # SerpAPI integration and data processing
    ├── generator.py         # CSV and Excel file generation
    └── exporter.py          # File download handler
```

---

## Prerequisites

- Python 3.10 or higher
- A [SerpAPI](https://serpapi.com) account and API key (for live mode)

---

## Installation

Clone the repository and install dependencies.

```bash
git clone https://github.com/your-username/mapgrab.git
cd mapgrab
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your SerpAPI key.

```
SERPAPI_KEY=your_serpapi_key_here
```

---

## Running Locally

```bash
python scrapper.py
```

The app will start at `http://localhost:5000`.

---

## API Reference

### GET /generate

Triggers a scrape and returns the filenames of the generated output files.

**Query Parameters**

| Parameter | Type   | Required | Description                          |
|-----------|--------|----------|--------------------------------------|
| `q`       | string | Yes      | Search query (e.g. `restaurants in Mumbai`) |

**Response**

```json
{
  "csv": "restaurants_in_mumbai_1712345678.csv",
  "excel": "restaurants_in_mumbai_1712345678.xlsx"
}
```

**Demo Mode**

Use `q=demoliveshowcase` to run against bundled sample data without consuming API credits.

---

### GET /download/`<filename>`

Downloads a previously generated file.

Only `.csv` and `.xlsx` files are served. All other file types return `403 Forbidden`.

---

## Output Fields

Each exported record contains the following columns:

| Column             | Description                          |
|--------------------|--------------------------------------|
| INDEX              | Row number (1 to 100)                |
| NAME               | Business name                        |
| ADDRESS            | Full address                         |
| PHONE_NUMBER       | Contact number                       |
| RATING             | Star rating                          |
| REVIEWS            | Number of reviews                    |
| PRICE              | Price range indicator                |
| TYPE               | Business category                    |
| OPERATING_HOURS    | Current open/close status            |
| GOOGLE_MAPS_LINK   | Direct Google Maps URL               |
| LATITUDE           | GPS latitude                         |
| LONGITUDE          | GPS longitude                        |

---

## Deployment

The project includes a `procfile` for deployment on platforms like Heroku or Railway.

```
web: gunicorn scrapper:app
```

Ensure the `SERPAPI_KEY` environment variable is set in your deployment environment.

---

## Dependencies

| Package        | Purpose                        |
|----------------|--------------------------------|
| `flask`        | Web framework                  |
| `gunicorn`     | Production WSGI server         |
| `requests`     | HTTP client for SerpAPI calls  |
| `python-dotenv`| Environment variable loading   |
| `openpyxl`     | Excel file generation          |

---

## Notes

- Each scrape fetches up to 5 pages of results (20 results per page) with a 1-second delay between requests to avoid rate limiting.
- Previously generated files in the `files/` directory are deleted at the start of each new scrape.
- The `files/` directory must exist before running the app.
