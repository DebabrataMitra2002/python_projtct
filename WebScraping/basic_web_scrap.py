# import requests
# from bs4 import BeautifulSoup as bs
# urls = requests.get('https://robu.in/')
# # print(urls.content)
# print(urls.url)
# print(urls.status_code)
# soup = bs(urls.text, "lxml")
# print(soup)
import requests
from bs4 import BeautifulSoup

def extract_paper_info(query):
    # Encode the query to include in the URL
    encoded_query = '+'.join(query.split())
    url = f"https://scholar.google.com/scholar?q={encoded_query}"

    # Send a GET request to Google Scholar
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract paper titles and authors' names
        titles = soup.find_all('h3', class_='gs_rt')
        authors = soup.find_all('div', class_='gs_a')
        
        # Print the extracted information
        for title, author in zip(titles, authors):
            paper_title = title.text
            authors_names = author.text
            print("Paper Title:", paper_title)
            print("Authors:", authors_names)
            print()
    else:
        print("Failed to retrieve data from Google Scholar.")

# Example usage
query = "natural language processing"
extract_paper_info(query)
