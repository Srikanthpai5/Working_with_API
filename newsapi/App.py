# https://newsapi.org/docs/client-libraries/python


from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="###")

    topheadlines = newsapi.get_top_headlines(sources="bbc-news,the-verge,fox-news,cnn",
                                                 language='en')

    articles = topheadlines['articles']

    tit = []
    desc = []
    img = []
    source = []

    for i in range(len(articles)):
        myarticles = articles[i]

        tit.append(myarticles['title'])
        source.append(myarticles['source']['name'])
        img.append(myarticles["urlToImage"])
        desc.append(myarticles['description'])


    mylist = zip(tit, source, desc, img)

    return render_template("index.html", context = mylist)

if __name__ == "__main__":
    app.run(debug=True)
