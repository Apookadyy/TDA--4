# 🚀 Automation Suite

A unified, command-line based Automation Suite designed to streamline repetitive operational tasks through modular automation tools.  
This project focuses on productivity, monitoring, and automation using Python.

---

## 📌 Project Overview

The Automation Suite integrates multiple automation utilities into a single, extensible system:

- 📁 File Organizer
- 🌐 Web Scraper
- 📧 Email Automation
- 🖥 System Monitor

### 🎯 Objectives
- Reduce manual effort through automation
- Provide real-time operational insights
- Maintain modular, scalable architecture
- Enable easy configuration and testing

---

## 🧰 Features

### 📁 File Organizer
- Monitors a target directory (e.g., Downloads)
- Categorizes files (Documents, Images, Videos, Others)
- Detects duplicate files using hashing
- Displays organization statistics

### 🌐 Web Scraper
- Multi-job scraping support
- Tracks pages scraped and data extracted
- Proxy rotation support
- Success rate monitoring

### 📧 Email Automation
- Template-based email generation
- Campaign scheduling
- Tracks open and click rates
- Supports bulk emailing

### 🖥 System Monitor
- Real-time CPU usage monitoring
- Memory, disk, and network tracking
- Alert-ready architecture

---

## 🏗️ Project Structure

```text
automation_suite/
├── main.py
├── file_organizer.py
├── web_scraper.py
├── email_automation.py
├── system_monitor.py
├── config.py
├── config.yaml
├── logs/
├── tests/
│   ├── test_file_organizer.py
│   ├── test_web_scraper.py
│   ├── test_email_automation.py
│   ├── test_system_monitor.py
│   ├── test_integration.py
│   └── test_config.py
└── README.md

# Clone the repository
git clone https://github.com/your-username/automation_suite.git

# Navigate to the project directory
cd automation_suite

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

