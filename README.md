# Introduction
This is an API service which retrieves UFO sighting entries from a sqlite3 database. Users can also retrieve these sightings via a REST API. 

This project requires Python3 and uses the following dependencies:
- sqlite3
- Flask
- BeautifulSoup4
- requests
- os

# Structural Overview
- `db` contains a blank `__init__` 
- `app` contains the other application files including a config file, an init file which includes the routing, and a scraper file. This directory also contains`template` and `static` directories for the basic HTML, JS, and CSS for the app. A frontend was not required, but creating a basic interface for the API was simple. With that said, I did not see a need to go overboard with the display creativity. 

# Primary Design Decisions
What was the goal of this project? To conveniently provide users with UFO sighting entries. Users can search for sightings based on the location (city, state, or country) as well as the occurring date.
## sqlite3
The dataset is homogenous, so I didn't think pulling out a non-relational db solution like MongoDB would be needed. Given the size of the data, even if I seeded the db with every entry from the link, sqlite3 fitted my needs. Serverless and accessible, this service improves DX. I don't think scalability would be an issues (a few large services use SQLite as their primary DB solution), a team with already provisioned resources might want to take advantage of MySQL. 

## Flask
Flask is a minimalistic web framework, which seemed to fit the needs of this project more than a robust fullstack framework such as Django. A frontend wasn't required and this framework enables static JS/HTML/CSS. 

## BeautifulSoup
The two candidates for a scraper were either Scrapy or BS4. Although the former offered more features and is actually considered a scraper, I did not need a robust solution for this project. Ultimately, the html parser module from BeautifulSoup in conjunction with requests sufficed.

## requests
This library in conjunction with BS4 allows for a more capable scraper. 




# Conclusion
This project was interesting. I haven't written many web-based Python projects in a while and I haven't had experience with Flask or SQLite until this, so it was fun reacquainting myself with these technologies.