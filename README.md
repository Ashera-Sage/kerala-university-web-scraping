# Kerala University Affiliated Colleges — Web Scraping

## Project Overview
This project uses Python web scraping to collect information about colleges affiliated with the University of Kerala from its official affiliated colleges directory.

## Objectives
- Analyze the structure of the college directory.
- Extract college information from individual college profiles.
- Clean and validate the extracted dataset.
- Perform exploratory data analysis and visualize contact information availability.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Jupyter Notebook

## Data Collected
The dataset contains the following fields:
- College Name
- Address
- Contact Number
- Email Address
- Website URL

## Project Files
- `Kerala_University_Web_Scraping.ipynb` — Notebook containing website analysis, extraction, data cleaning, visualizations, and findings.
- `kerala_university_scraper.py` — Standalone Python scraping script.
- `kerala_university_colleges.csv` — Extracted college dataset.

## Summary
A total of 204 college records were extracted. The cleaned dataset contains 26 missing email addresses and 13 missing contact numbers. No duplicate rows or duplicate college names were detected.

## How to Run
1. Install the required libraries:

   `pip install requests beautifulsoup4 pandas matplotlib`

2. Run the scraper:

   `python kerala_university_scraper.py`

3. Open the Jupyter Notebook to explore the analysis and visualizations.

## Data Source
[University of Kerala — Affiliated Colleges](https://www.keralauniversity.ac.in/affiliated-colleges)

## Note
Contact information and website URLs were checked for completeness and basic formatting. Their real-world accuracy and accessibility have not been independently verified.
