"""
We want a class that sends request to a given url  ( Test for RMV)
pull scrape data from rightmove 
write on database ( save as csv )
dataframe: link, price, no_of_bedrooms, address, city, country


https://stackoverflow.com/questions/36662524/rightmove-api-and-scraping-technical-and-legal

"""
import requests

class UrlRequester:
    def __init__(self):
        self.session = requests.Session()

    def send_get_request(self, url, params=None, headers=None):
        try:
            response = self.session.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    def send_post_request(self, url, data=None, json=None, headers=None):
        try:
            response = self.session.post(url, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    # Create an instance of UrlRequester
    requester = UrlRequester()

    # Send a GET request
    get_response = requester.send_get_request("https://jsonplaceholder.typicode.com/posts/1")
    print("GET Response:")
    print(get_response)

    # Send a POST request
    post_data = {"title": "foo", "body": "bar", "userId": 1}
    post_response = requester.send_post_request("https://jsonplaceholder.typicode.com/posts", json=post_data)
    print("POST Response:")
    print(post_response)
