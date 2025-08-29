"""
streamlit run Web_Scraping_Tool_v2.py

https://stackoverflow.com/questions/36662524/rightmove-api-and-scraping-technical-and-legal
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
                scraped_links = scraper.scrape(custom_url)
                if scraped_links:
                    st.header("Scraped Links:")
                    for link in scraped_links:
                        st.write(link)

                    # Add functionality to store and download the data
                    if st.button("Download Data"):
                        with open("scraped_links.txt", "w") as file:
                            for link in scraped_links:
                                file.write(link + "\n")
                        st.success("Data has been downloaded as 'scraped_links.txt'.")
                else:
                    st.warning("No links were scraped.")
            else:
                st.warning("Please enter a valid URL.")
    elif option == "Use a predefined URL":
        predefined_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=1250000&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'  # Replace with your predefined URL
        if st.button("Scrape predefined URL"):
            scraped_links = scraper.scrape(predefined_url)
            if scraped_links:
                st.header("Scraped Links:")
                for link in scraped_links:
                    st.write(link)

                # Add functionality to store and download the data
                if st.button("Download Data"):
                    with open("scraped_links.txt", "w") as file:
                        for link in scraped_links:
                            file.write(link + "\n")
                    st.success("Data has been downloaded as 'scraped_links.txt'.")
            else:
                st.warning("No links were scraped.")

if __name__ == "__main__":
    main()
