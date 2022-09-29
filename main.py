import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from product import Product
from sys import argv

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

products_above_4_stars = []

def search(searchterm: str):
    # init webdriver
    driver = webdriver.Chrome(options=options)
    # open amazon.de return search results
    driver.get(f"https://www.amazon.de/s?k={searchterm.replace(' ', '+')}")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type':'s-search-result'})
    print(f"Found {len(results)} results for {searchterm}")    
    driver.close()
    return results

def create_product(product) -> Product:
    """
    Takes a bs4.element.Tag and returns a Product object.
    """
    
    try:
        name = product.img.get('alt')
        image = product.find('img', {'class':'s-image'}).get('src')
        stars = product.i.text
        ratings = product.find('span', {'class':'a-size-base s-underline-text'}).text
        price = product.find('span', {'class':'a-price'}).find('span', {'class':'a-offscreen'}).text
        url = "https://www.amazon.de" + product.h2.a.get('href')
        
        product = Product(
        name,
        image, 
        stars, 
        ratings,
        price,
        url
        )
        print("Created product:", product)
    except Exception as e:
        # print("Error:", str(e), product)
        pass
    return product
    
def filter_four_stars_and_more(products: list) -> list:
    """
    Takes a list of search results and returns only objects with a ratings bigger
    then 4 stars.
    """
    for product in products:
        if product != None:
            rating_as_float = float(product.stars[0:3].replace(',', '.'))
            if rating_as_float >= 4.0:
                products_above_4_stars.append(product)
        else:
            return
        
def my_fav(results: list) -> Product:
    """
    Searches the list for the product with at least four stars rating BUT the
    ratings.
    """
    
    favourite_product = ""
    
    for product in products_above_4_stars:
        if favourite_product == "":
            favourite_product = product
            print("My Fav Product:", favourite_product)
        elif float(favourite_product.ratings) < float(product.ratings) and float(favourite_product.stars[:3].replace(",", ".")) < float(product.stars[:3].replace(",", ".")):
            favourite_product = product
            print("My New Fav Product:", favourite_product)
            
    return my_fav
            
def most_rated(products: list):
    """
    Product with the most ratings.
    """
    pass

def most_expensive(products: list) -> Product:
    """
    The most expensive price.
    """
    pass

def cheapest(products: list) -> Product:
    """
    The cheapest best rated Product.
    """
    cheapest = ""
    for product in products:
        if product:
            if cheapest == "":
                cheapest = product
                print("Cheapest Product:", cheapest)
            # elif float(cheapest.price[:4]) >= float(product.price[:4]) and float(cheapest.ratings) <= float(product.ratings) and float(cheapest.stars[:3].replace(",", ".")) <= float(product.stars[:3].replace(",", ".")):
            elif float(cheapest.price.split()[0].replace(",", ".")) > float(product.price.split()[0].replace(",", ".")):
                cheapest = product
                print("New Cheapest Product:", cheapest)
        else:
            return
    return cheapest

if __name__ == '__main__':
    results = search(argv[1])
    products = list(map(create_product, results))
    # for product in products:
    #     print(product)
        
    # filter_four_stars_and_more(products)
    # print(products_above_4_stars)
    # my_fav(products_above_4_stars)
    print("Cheapest", cheapest(products))
    
