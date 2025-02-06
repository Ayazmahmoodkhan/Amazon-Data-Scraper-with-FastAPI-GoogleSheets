# Amazon-Data-Scraper-with-FastAPI-GoogleSheets

A powerful and automated web scraping API that fetches real-time data from e-commerce platforms, processes it, and stores the results in Google Sheets. Built using Scrapy and FastAPI, this project enables seamless data extraction, dynamic API responses, and efficient background task execution.

# 🕵️‍♂️ Smart Scraper API – Automated Web Scraping & API Integration

## 🚀 **Overview**

This project provides an **automated web scraping solution** integrated with an API to retrieve and update product data dynamically. If data is unavailable, the scraper **automatically triggers** to fetch fresh results. The data is processed and stored in **Google Sheets** for easy access.

## 🛠 **Features**

✅ **Scrapy-based Web Scraper** – Extracts real-time product data from e-commerce websites  
✅ **FastAPI Integration** – Exposes scraped data via RESTful API  
✅ **Google Sheets Integration** – Saves and retrieves data in structured format  
✅ **Background Task Execution** – Runs the scraper asynchronously without blocking API requests  
✅ **Auto-Retriggering Scraper** – If data isn't found, the scraper is triggered dynamically

## 🔧 **Tech Stack**

- **Python 3.9+**
- **Scrapy** (Web Scraping)
- **FastAPI** (API Development)
- **Google Sheets API** (Data Storage)
- **Subprocess & BackgroundTasks** (Automation)

## 🚀 **How It Works**

1. **API Request**: A client requests product data using the `/products/?keyword={query}` endpoint.
2. **Data Check**: If data exists in Google Sheets, it is returned instantly.
3. **Scraper Trigger**: If no data is found, the **scraper is automatically triggered** to fetch fresh results.
4. **Data Storage**: Scraped data is stored in Google Sheets for future use.

## ⚡ **Setup & Installation**

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/Amazon-Data-Scraper-with-FastAPI-GoogleSheets.git
cd Amazon-Data-Scraper-with-FastAPI-GoogleSheets
🔹 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 3. Run FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload
🔹 4. Start Scrapy Spider (Optional)
scrapy crawl amazon_search -a keyword="iphone"
📡 API Endpoints
Method	Endpoint	Description
GET	/products/?keyword={query}	Fetch product data for a given keyword
POST	/trigger-scraper/	Manually trigger the scraper
🎯 Future Enhancements
🔹 Multi-platform support (eBay, Walmart, etc.)
🔹 Database storage (MongoDB/PostgreSQL)
🔹 Enhanced error handling & logging

💡 Contributing
Want to improve this project? Contributions are welcome! Feel free to fork, open an issue, or submit a pull request.

📜 License
This project is open-source and available under the MIT License.

📬 Connect with Me
🔗 LinkedIn:https://www.linkedin.com/in/ayaz-mahmood-583963207/
📧 Email: ayazmahmood@gmail.com

🚀 Star this repo if you found it useful! ⭐

This README follows best practices and makes your GitHub project **clear, professional, and enga
```
