from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Initializing the driver
def initialise_driver():    
    driver = webdriver.Chrome()
    return driver

# Function to open yellow page
def open_yellow_page(driver, search_query='restaurants', location='new york'):
    location = location.replace(" ", "+")
    url = f'https://www.yellowpages.com/search?search_terms={search_query}&geo_location_terms={location}'
    driver.get(url)
    time.sleep(2)
    print(f"Opened Yellow Page for '{search_query}' in '{location}'.")

# Function to extract business details from Yellow Page
def extract_business_details(driver):
    business_data = []
    try:
        businesses_list = driver.find_elements(By.XPATH, "//div[@class='srp-listing clickable-area mdm']")
        if not businesses_list:
            print("No businesses found on this page.")
            return []

        for business in businesses_list:
            # Name of the business
            name = business.find_element(By.XPATH, ".//a[@class='business-name']/span").text

            # Phone number
            ph_no = business.find_element(By.XPATH, ".//div[@class='phones phone primary']").text

            # Website URL
            website_links = business.find_elements(By.XPATH, ".//div[@class='links']/a[@class='track-visit-website']")
            website_link = website_links[0].get_attribute('href') if website_links else 'No website link available'

            # Address of the business
            address = business.find_element(By.XPATH, ".//div[@class='adr']").text

            # Collect the data
            business_data.append((name, ph_no, website_link, address))
    
    except Exception as e:
        print(f"Error extracting business details: {e}")
    
    return business_data

# Function to go to next page
def next_page(driver):
    try:
        next_button = driver.find_elements(By.XPATH, "//a[@class='next ajax-page']")
        if next_button:
            next_url = next_button[0].get_attribute('href')
            if next_url:
                driver.get(next_url)
                time.sleep(2)
                print("Moved to next page.")
                return True
        print("No next page available.")
        return False
    except Exception as e:
        print(f"Error moving to next page: {e}")
        return False

# Function to save all extracted data in CSV
def save_to_csv(data, filename='businesses.csv'):
    if not filename.endswith('.csv'):
        filename += '.csv'
    if data:
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Phone Number', 'Website', 'Address'])
                writer.writerows(data)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
    else:
        print("No data to save.")

# Main function
def main():
    yellow_page_opened = False
    driver = None
    all_business_data = []

    while True:
        print("\nMenu:")
        print("1. Open Yellow Page")
        print("2. Extract Business Data")
        print("3. Save Data to CSV")
        print("4. Go to Next Page")
        print("5. Exit")

        try:
            ch = input("Enter your choice (1-5): ")
            ch = int(ch)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if ch == 1:
            if driver is None:
                driver = initialise_driver()
            if not yellow_page_opened:
                search_query = input("Enter search query (e.g., restaurants, plumbers, doctors, etc.): ")
                location = input("Enter location (e.g., New York): ")

                if not search_query:
                    search_query = 'restaurants'
                if not location:
                    location = 'new york'

                open_yellow_page(driver, search_query, location)
                yellow_page_opened = True
            else:
                print("Yellow page is already opened.")

        elif ch == 2:
            if driver is not None and yellow_page_opened:
                print("Extracting business data from the current page...")
                business_data = extract_business_details(driver)
                if business_data:
                    all_business_data.extend(business_data)
                    print(f"Extracted {len(business_data)} business(es) data from the current page.")
                else:
                    print("No business data found on this page.")
            else:
                print("Please open Yellow page first.")

        elif ch == 3:
            filename = input("Enter filename to save data (default 'businesses.csv'): ")
            if not filename:
                filename = 'businesses.csv'
            if all_business_data:
                save_to_csv(all_business_data, filename)
            else:
                print("No data to save.")

        elif ch == 4:
            if driver is not None and yellow_page_opened:
                if not next_page(driver):
                    print("No next page is available.")
            else:
                print("Please open Yellow page first.")

        elif ch == 5:
            if driver:
                driver.quit()
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
