import requests
from parsel import Selector
import random

with open("proxies.txt", "r") as file:
    proxies = [line.strip() for line in file]

proxy = random.choice(proxies)

f = open("list.csv", "a")

#url = "https://www.bol.com/nl/nl/l/bouwsets/20001/?bltgh=nE37DKNEXhhpUQqKA4VDuA.2_20_21.22.CategoryImage"
url = "https://www.bol.com/nl/nl/l/boeken/8299/"
response = requests.get(url, proxies={"http": proxy})
html = response.text

selector = Selector(text=html)

product_containers = selector.xpath('//li[contains(@class, "product-item")]')
print(f"using {proxy}")
for product in product_containers:
    try:
        
        name = product.xpath('.//a[@data-test="product-title"]/text()').get()
        price = product.xpath('.//span[@data-test="price"]/text()').get('')
        link = product.xpath('.//a[@data-test="product-title"]/@href').get()
        author = product.xpath('.//a[@itemprop="name"]/text()').get()
        category = product.xpath('//p[@data-test="breadcrumb-name"]/text()').get()
        amount_of_ratings = product.xpath('.//div[@class="star-rating"]/@data-count').get()
        rating = product.xpath('.//div[@class="star-rating"]/@title').get()
        pid = product.xpath('.//wsp-comparable/@data-product-id').get()
        print(f"\nRatings: {rating.strip()}({amount_of_ratings})\nCategory: {category.strip()}\nAuthor: {author.strip()}\nName: {name.strip()} PID: {pid.strip()}\nPrice: €{price.strip()}\nURL: https://bol.com{link.strip()}\n")
        #f.write(f"\nRatings: {rating.strip()}({amount_of_ratings})\nCategory: {category.strip()}\nAuthor: {author.strip()}\nName: {name.strip()} PID: {pid.strip()}\nPrice: €{price.strip()}\nURL: https://bol.com{link.strip()}\n")
    except:
        continue
#print(html)
f.close()

