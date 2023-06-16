import requests as req
print("import all modules successfully")

proxies = {
    'https': 'http://salah213:BFwq7XeP8BM26IAR@proxy.packetstream.io:31112/'
}

URLs = [
    "https://mind-valleey.com/products.json",
    "https://hammerboxofficial.com/products.json",
    "https://bleame.com/products.json"
]

for url in URLs:
    response = req.get(url, proxies=proxies)
    data = response.json()
    products = data['products']
    for product in products:
        # write into a file
        file = open("products.txt", "a")
        file.write("Title : " + product['title'] + "\n")
        
        # print("Title : " + product['title'])
        # print("Updated at : " + product['updated_at'])
        # print("Vendor : " + product['vendor'])
        # print("---------------------------------")

# print content of the file
file = open("products.txt", "r")
print(file.read())

    

        


