# main.py

import logging
from datetime import datetime

from file_organizer.organizer import organize_files
from web_scraper.scraper import run_scraper
from email_automation.sender import email_status
import system_monitor.monitor 

# Configure logging
logging.basicConfig(
    filename="automation_suite.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    logging.info("=== Automation Suite Started ===")

    # List of tasks as tuples: (function, task_name)
    tasks = [
        (organize_files, "File Organizer"),
        (run_scraper, "Web Scraper"),
        (email_status, "Email Automation"),
        (system_monitor.monitor.system_status, "System Monitor")
    ]

    for func, name in tasks:
        try:
            logging.info(f"Starting task: {name}")
            func()
            logging.info(f"Task completed successfully: {name}")
        except Exception as e:
            logging.error(f"Task failed: {name} | Error: {e}")

    logging.info("=== Automation Suite Finished ===")


if __name__ == "__main__":
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    logging.info(f"Total runtime: {end_time - start_time}")
