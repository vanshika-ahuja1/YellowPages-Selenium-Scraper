# YellowPages Selenium Scraper

A **menu-driven** Python web scraper that leverages **Selenium** to extract business listings such as restaurants, services, and more from YellowPages.com. The scraper allows users to search businesses by keywords and locations, navigate through multiple result pages, and save the extracted data into a CSV file.

## Key Features

- **Interactive, Menu-Driven Program**: Offers a simple CLI interface with menu options to perform different tasks.
- **Selenium Automation**: Uses Selenium WebDriver for browser automation to load pages and extract data.
- **Customizable Search**: Allows users to search for businesses using any keyword (e.g., "restaurants", "plumbers") and location (e.g., "New York", "Los Angeles").
- **Extracted Information**:
  - Business Name
  - Phone Number
  - Website URL
  - Address
- **Data Saving**: The extracted data is saved in a CSV file for further analysis or record-keeping.
- **Multi-page Scraping**: Navigate through multiple YellowPages result pages to extract data from all available listings.

## Requirements

To run this script, you'll need:

- **Python 3.x**
- **Selenium**: For browser automation to interact with YellowPages.
- **ChromeDriver**: Required for Selenium to interact with the Google Chrome browser.
- **CSV**: For saving extracted data in CSV format.

To install the required Python packages:

```pip install selenium```

## How to Use

**1.Run the script:**

```python yellow_pages_business_search.py```

**2.Menu-Driven Interface:**
Once the program starts, it will display a menu with the following options:

* Open YellowPage: Opens YellowPages based on the provided search query (e.g., "restaurants") and location (e.g., "New York").
* Extract Data: Scrapes the data from the current page of the search results.
* Save Data to CSV: Saves all collected data to a CSV file (you can specify the filename).
* Go to Next Page: Moves to the next page of results and extracts more data.
* Exit: Exits the program.
  
Follow the prompts:

You will be prompted to enter a search term (e.g., "restaurants", "plumbers") and a location (e.g., "New York", "Los Angeles"). If left blank, defaults will be used.
After extracting data, you can save it in a CSV file by specifying the file name.
Example:
```
Enter your choice (1-5): 1
Enter search query (By default 'restaurants'): 
Enter location (By default 'New York'): 
opened yellow page successfully

Enter your choice (1-5): 2
Extracted 30 restaurants data from current page.

Enter your choice (1-5): 3
Enter filename to save data (default 'business.csv'): restaurants.csv
Data saved to yellow_pages_data.csv

Enter your choice (1-5): 5
```
This will save the data to a file named ```restaurants.csv.```

### Why This README Is Effective:

- **Clear and Structured**: It’s divided into sections that explain different aspects of the repository.
- **Menu Explanation**: It goes in-depth into how the menu options work so users understand the flow of the program.
- **Selenium Emphasis**: It clearly mentions the use of Selenium, which is the key technology behind this project.
- **User-Friendly**: Simple step-by-step instructions make it easy for anyone, even beginners, to run the script.







