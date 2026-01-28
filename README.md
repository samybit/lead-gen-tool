# 🛒 E-Commerce Data Extraction Tool (SaaS)

A production-ready data pipeline that automates the extraction, cleaning, and formatting of e-commerce product data. Built for market researchers and dropshippers who need decision-ready data in Excel format.

**[🔴 Live Demo Link](http://samyrai.pythonanywhere.com)**

## 🚀 Key Features
* **Multi-Page Crawling:** Automatically detects pagination and scrapes entire categories, not just single pages.
* **Auto-Cleaning Pipeline:** Converts raw currency strings (e.g., `£51.77`) into calculable floats and strips non-numeric characters.
* **In-Memory Processing:** Uses `io.BytesIO` to generate files in RAM, ensuring high performance and stateless server operation.
* **Dockerized:** Includes a production-ready `Dockerfile` for containerized deployment on any cloud provider (AWS, Azure, Render).
* **Excel Export:** Delivers native `.xlsx` files using Pandas and OpenPyXL.

## 🛠️ Tech Stack
* **Core:** Python 3.11, Flask
* **Data Processing:** Pandas, NumPy
* **Scraping:** BeautifulSoup4, Requests
* **Infrastructure:** Docker, Gunicorn (Ready), PythonAnywhere

## 📦 Local Installation (Docker)
This project is containerized for easy setup.

```bash
# 1. Build the image
docker build -t lead-gen-tool .

# 2. Run the container
docker run -p 5000:5000 lead-gen-tool
```

📄 License
MIT License. Free for commercial and private use.
