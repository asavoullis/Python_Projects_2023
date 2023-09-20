"""
streamlit run Webscraping.py
"""

import requests
from bs4 import BeautifulSoup
import streamlit as st

class WebScraper:
    def __init__(self):
        pass

    def scrape(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            return [link.get('href') for link in links]
        else:
            return []

def main():
    st.title("Web Scraper with Streamlit")
    scraper = WebScraper()

    option = st.radio("Choose an option:", ["Enter a custom URL", "Use a predefined URL"])

    if option == "Enter a custom URL":
        custom_url = st.text_input("Enter the URL you want to scrape:")
        if st.button("Scrape"):
            if custom_url:
                st.header("Scraped Links:")
                scraped_links = scraper.scrape(custom_url)
                for link in scraped_links:
                    st.write(link)
            else:
                st.warning("Please enter a valid URL.")
    elif option == "Use a predefined URL":
        predefined_url = 'https://example.com'  # Replace with your predefined URL
        if st.button("Scrape predefined URL"):
            st.header("Scraped Links:")
            scraped_links = scraper.scrape(predefined_url)
            for link in scraped_links:
                st.write(link)

if __name__ == "__main__":
    main()
