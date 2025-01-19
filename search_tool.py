import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def fetch_results(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("div", {"class": "result-item"})
    except requests.RequestException as e:
        print(f"Error fetching results from {url}: {e}")
        return []

def search_data(query):
    # Search on public records websites
    public_records_url = "https://www.publicrecords.com/search?query=" + query
    public_records_results = fetch_results(public_records_url)
    
    # Search on social media platforms
    social_media_url = "https://social-searcher.com/search?q=" + query
    driver = webdriver.Chrome()
    try:
        driver.get(social_media_url)
        time.sleep(5)  # Wait for the page to load
        social_media_results = driver.find_elements_by_css_selector(".result-item")
    except Exception as e:
        print(f"Error searching social media: {e}")
        social_media_results = []
    finally:
        driver.quit()  # Ensure the browser is closed
    
    # Search on online directories
    online_directories_url = "https://ahmia.fi/search/?q=" + query
    online_directories_results = fetch_results(online_directories_url)
    
    # Search on dark web databases
    dark_web_url = "https://darksearch.io/search?q=" + query
    dark_web_results = fetch_results(dark_web_url)
    
    # Combine and return the search results
    results = {
        "Public Records": public_records_results,
        "Social Media": social_media_results,
        "Online Directories": online_directories_results,
        "Dark Web Databases": dark_web_results
    }
    return results

# Example usage
query = "john.doe@example.com"
search_results = search_data(query)
print("Search Results:")
for source, results in search_results.items():
    print(f"\n{source}:")
    for result in results:
        print(result.text)