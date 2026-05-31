# Capstone Project: Zillow to Google Forms Data Entry Automation

This Python script automates the process of scraping rental property listings from a Zillow-clone website and automatically populating a Google Form with the collected data.

## Features

- Scrapes rental listings, addresses, prices, and links using **BeautifulSoup**.
- Automates Google Form submissions using **Selenium Webdriver**.
- Stores configuration variables (like the Google Form URL) securely using environment variables (`.env`).

## Prerequisites

Make sure you have Python 3 installed. You will also need Google Chrome installed, as the script uses Chrome WebDriver via Selenium.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Capstone-project
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your environment variables:**
   - Copy `.env.example` to create a `.env` file:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and replace `your_google_form_link_here` with your actual Google Form URL:
     ```env
     FORM_LINK=https://docs.google.com/forms/...
     ```

## Running the Script

Execute the Python script:
```bash
python app.py
```

The script will fetch the listings and then launch a Selenium Chrome instance to automatically fill in the Google Form for each listing.
