from flask import Flask,render_template,request
import requests
from config import NEWS_API_KEY

#create a Flask Application
app = Flask(__name__)

#HomePage - Route
@app.route("/")
def index():
    query = request.args.get("query","lastest")
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get('articles',[])
    return render_template('index.html',articles=articles)



if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')