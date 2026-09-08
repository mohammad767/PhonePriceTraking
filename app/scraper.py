import requests
from bs4 import BeautifulSoup
from utils import clean_price
from rich.pretty import pprint
from models import Product



def technolife_scraper():
   
    base_url = "https://www.technolife.com"
    url = "https://www.technolife.com/category/mobile/mobile-phone"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try : 
        response = requests.get(url, headers=headers, timeout=20)
    except requests.Timeout:
            print("Error: The request timed out while trying to retrieve the webpage.")
            return []
        
    except requests.ConnectionError:
            print("Error: Connection error occurred while trying to retrieve the webpage.")
            return []
        
    except requests.RequestException as e:
        print("Error: Failed to retrieve the webpage.")
        return []
   
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")
        if not articles:
            print("Error: No articles found on the webpage.")
            return []
        
        article = articles[0]  
        product_list = []
        for phone in article :
             
            
            name_tag = phone.find("h2")
            if not name_tag:
                print("Error: Could not find the name tag for a phone.")
                continue
            name = name_tag.get_text(strip=True)
            
            
            price_tag = phone.find("p", class_="text-[22px]")
            if not price_tag:
                print("Error: Could not find the price tag for a phone.")
                continue
            price = price_tag.get_text(strip=True)
            price = clean_price(price)
            
            
            url_tag = phone.find("a")
            if not url_tag or not url_tag.get("href"):
                print("Error: Could not find the link for a phone.")
                continue
            url = base_url + url_tag["href"]
            product_obj = Product(name,price,url)
            product_list.append(product_obj)

                       
        
    elif response.status_code == 404:
        print("Error: The requested webpage was not found (404).")
        return []
    elif response.status_code == 403:
        print("Error: Access to the webpage is forbidden (403).")
        return []
    elif response.status_code == 500:
        print("Error: Internal server error occurred (500).")
        return []
    else : 
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []
        
    return product_list

