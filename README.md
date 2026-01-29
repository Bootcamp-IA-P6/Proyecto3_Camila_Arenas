# 🕸️ Django Web Scraper with Docker & Cron

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0-43B02A?logo=selenium&logoColor=white)

## 📖 About the Project

This is an automated web scraping application built with **Django** and **Selenium**, fully containerized using **Docker**.

It is designed to:
- 🕵️‍♂️ **Scrape data** from websites automatically.
- 📸 Take **debug screenshots** of the target pages.
- ⏰ Run periodically (every 5 minutes) using a **Cronjob**.
- 💾 Store the extracted data in a **SQLite** database.

## 🚀 Features

- **Dockerized Environment:** Easy setup with `docker compose`.
- **Headless Browser:** Uses Firefox via GeckoDriver in headless mode.
- **Automated Scheduling:** Configured with Linux `cron` to run the scraper every 5 minutes.
- **Persistence:** Data is saved to `db.sqlite3` and screenshots are saved to a local volume to persist after container restarts.
- **Error Handling:** Captures screenshots when elements are found (or on errors) for easier debugging.

## 🛠️ Installation & Usage

### Prerequisites
- Docker and Docker Compose installed on your machine.

### How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bootcamp-IA-P6/Proyecto3_Camila_Arenas.git
   cd webscraper

2. **Build and Start the Container:**
   ```bash
   docker compose up --build
   ```
   *The scraper will start automatically in the background.*

3. **Verify Execution:**
   You can check the cron logs inside the container to see the scraper activity:
   ```bash
   docker exec -it webscraper-server-1 cat /var/log/cron.log
   ```

4. **View Screenshots:**
   Check the generated `./screenshots` folder in your project root to see the browser captures created during execution.
  <img width="433" height="291" alt="image" src="https://github.com/user-attachments/assets/1f2dcb32-129f-4b29-9d6e-8f3053077e5c" />

## 📂 Project Structure

```text
.
├── Dockerfile           # Docker configuration
├── compose.yaml         # Docker Compose services
├── cronfile             # Crontab schedule
├── requirements.txt     # Python dependencies
└── webscraper_project/  # Django application
    ├── manage.py
    └── scraper/
        ├── services/
        │   └── scrape.py
        └── models.py
```
## 📝 Authors
- **[Camila Arenas](https://github.com/mcarenashd)** - *Initial work* 
