import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

conn = sqlite3.connect('db/search_sightings.db')
cursor = conn.cursor()


def extract_subentry_info(subentry, second_arg):
    cols = subentry.find_all('td')
    date_occurred = cols[1].text
    city = cols[2].text if cols[2].text else None
    state = cols[3].text if cols[3].text else None
    country = cols[4].text if cols[4].text else None
    shape = cols[5].text if cols[5].text else None
    summary = cols[6].text if cols[4].text else None
    return {
        "date_occurred": date_occurred,
        "date_posted": second_arg,
        "city": city,
        "state": state,
        "country": country,
        "shape": shape,
        "summary": summary,
    }


def scrapeit():
    print('Scraping UFO data from link')
    # Step 1: Make an HTTP request to the URL
    url = "https://nuforc.org/ndx/?id=event"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        date_table = soup.find("table")
        date_links = [a for a in date_table.find_all("a")]
        for i in date_links[0:3]:
            second_arg = i.text
            date_url = "https://nuforc.org/" + i['href']
            date_response = requests.get(date_url)

            if date_response.status_code == 200:
                date_soup = BeautifulSoup(date_response.text, "html.parser")
                tables = date_soup.find("table")
                subentries = tables.find_all("tr")[1:len(tables)-1]  # Skip the header row and the last row
                for subentry in subentries:
                    subentry_info = extract_subentry_info(subentry, second_arg)
                    # Check if the data already exists in the database
                    clean = subentry_info['date_occurred'].split(" ")[0]
                    entry_date = datetime.datetime.strptime(clean, "%m/%d/%Y")
                    current_date = datetime.datetime.now()
                    if entry_date <= current_date:
                        cursor.execute('''
                            SELECT * FROM ufo_sightings 
                            WHERE date_occurred = ? 
                            AND date_posted = ?
                            AND city = ? 
                            AND state = ? 
                            AND country = ? 
                            AND shape = ? 
                            AND summary = ?
                        ''', (
                            subentry_info["date_occurred"],
                            subentry_info["date_posted"],
                            subentry_info["city"],
                            subentry_info["state"],
                            subentry_info["country"],
                            subentry_info["shape"],
                            subentry_info["summary"]
                        ))
                        existing_data = cursor.fetchone()
                        if existing_data is None:
                            cursor.execute('''
                                INSERT INTO ufo_sightings (date_occurred, date_posted, city, state, country, shape, summary)
                                VALUES (?, ?, ?, ?, ?, ?, ?)
                            ''', (
                                subentry_info["date_occurred"],
                                subentry_info["date_posted"],
                                subentry_info["city"],
                                subentry_info["state"],
                                subentry_info["country"],
                                subentry_info["shape"],
                                subentry_info["summary"]
                            ))

                            conn.commit()
                else:
                    print("Data already exists in the database.")

            else:
                print(f"Failed to fetch data from date link: {date_url}")
    else:
        print("Failed to fetch data from the main URL.")
