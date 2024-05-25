import requests
import json
query=input("What type of news you are intrested in? ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-04-29&sortBy=publishedAt&apiKey=3164c4a612b34b57a0ecba53992f32d9"
r=requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
 print(article["title"])
 print(article["description"])
 print("--------------------------------------------")

