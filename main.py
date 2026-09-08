import requests
from bs4 import BeautifulSoup

url = "https://www.technolife.com/category/mobile/mobile-phone"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")
    article = articles[0]  
    name = article.find("h2").get_text(strip=True)

    price = article.find(
        "p",
        class_="text-[22px] font-semiBold leading-5 text-primary-shade-1"
    ).get_text(strip=True)

    print("Name:", name)
    print("Price:", price)
    
else : 
    print("Failed to retrieve the webpage. Status code:", response.status_code)