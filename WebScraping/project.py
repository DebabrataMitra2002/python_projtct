import requests
from bs4 import BeautifulSoup

def extract_paper_info(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the articles in the webpage
        articles = soup.find_all('article')
        
        # Iterate over each article to extract title and author information
        for article in articles:
            # Extract paper title
            title_element = article.find('h2')
            paper_title = title_element.text.strip() if title_element else "Title not found"
            
            # Extract authors' names
            authors_element = article.find('p', class_='author')
            authors_names = authors_element.text.strip() if authors_element else "Authors not found"
            
            # Print the extracted information
            print("Paper Title:", paper_title)
            print("Authors:", authors_names)
            print()
    else:
        print("Failed to retrieve data from the webpage.")

# URL of the webpage containing the computer magazine information
url = "https://www.yogsutra.com/bangladeshi-computer-magazines.html"
extract_paper_info(url)
