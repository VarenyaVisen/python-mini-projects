from dotenv import load_dotenv
import os
import requests # pip install requests

query = input("What type of news are you interested in today? ")
load_dotenv()
api = os.getenv("NEWS_API_KEY")

from datetime import datetime, timedelta
date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
url = f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey={api}"


print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
