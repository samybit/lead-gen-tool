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

## 📦 Installation (Docker)
This project is containerized for easy setup.
1. Pull the pre-built image from Registry
```bash
docker pull ghcr.io/samybit/lead-gen-tool:latest
```
2. Run the container
```bash
docker run -p 5000:5000 ghcr.io/samybit/lead-gen-tool:latest
```
_Or_
1. Clone the repo
```bash
git clone https://github.com/samybit/lead-gen-tool.git
```
2. Build the image from the source code
```bash
cd lead-gen-tool
```
```bash
docker build -t lead-gen-tool .
```
3. Run the container
```bash
docker run -p 5000:5000 lead-gen-tool
```
🌍 Access the Tool
Once running, open your browser and visit: http://localhost:5000

## 📄 License
MIT License. Free for commercial and private use.
