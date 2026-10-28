
import requests
from bs4 import BeautifulSoup
import pandas as pd

# University affiliated colleges directory
url = "https://www.keralauniversity.ac.in/affiliated-colleges"

# Create a session and open the directory
session = requests.Session()
response = session.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find all college listings
college_items = soup.select("div.school-list-item")

# Details page URL
details_url = "https://www.keralauniversity.ac.in/affiliated-college-details"

# Store extracted records
all_colleges = []

for index, item in enumerate(college_items, start=1):
    try:
        form = item.find(
            "form",
            action="affiliated-college-details"
        )

        if not form:
            continue

        hidden_input = form.find(
            "input",
            {"name": "collegeCol"}
        )

        if not hidden_input:
            continue

        college_id = hidden_input.get("value")

        # Submit the form to retrieve the profile
        profile_response = session.post(
            details_url,
            data={"collegeCol": college_id},
            headers={"Referer": url},
            timeout=30
        )
        profile_response.raise_for_status()

        profile_soup = BeautifulSoup(
            profile_response.text,
            "html.parser"
        )

        info = profile_soup.find(
            "div",
            class_="category-list"
        )

        if not info or not info.find("h2"):
            print(f"Profile not found: {index}")
            continue

        college_name = info.find("h2").get_text(strip=True)

        contact_section = info.find("span")
        contact_text = (
            contact_section.get_text(" ", strip=True)
            if contact_section else ""
        )

        # Extract address
        address = None
        if "Contact Address :" in contact_text:
            address = contact_text.split(
                "Contact Address :", 1
            )[1].split("Contact No :", 1)[0].strip()

        # Extract contact number
        phone = None
        if "Contact No :" in contact_text:
            phone = contact_text.split(
                "Contact No :", 1
            )[1].split("Email :", 1)[0].strip()

        # Extract email
        email = None
        if "Email :" in contact_text:
            email = contact_text.split(
                "Email :", 1
            )[1].split("Web URL :", 1)[0].strip()

        # Extract website URL
        website_link = (
            contact_section.find("a", href=True)
            if contact_section else None
        )
        website_url = (
            website_link["href"] if website_link else None
        )

        all_colleges.append({
            "College Name": college_name,
            "Address": address,
            "Contact Number": phone,
            "Email Address": email,
            "Website URL": website_url
        })

        print(f"Processed {index}/{len(college_items)}")

    except requests.RequestException as error:
        print(f"Request failed for listing {index}: {error}")

# Create and save the dataset
df = pd.DataFrame(all_colleges)

df.to_csv(
    "kerala_university_colleges.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nScraping completed.")
print("College records extracted:", len(df))
print("CSV file: kerala_university_colleges.csv")
