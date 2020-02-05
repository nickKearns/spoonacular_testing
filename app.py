from flask import Flask, render_template, request
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SPOON_API_KEY')


app = Flask(__name__, static_url_path='/static')



@app.route('/')
def index():
    # search_term = request.args.get('user_input')
    
    params = {
        'query': "burger",
        'apiKey': api_key,
        'number': 10
    }


    r = requests.get("https://api.spoonacular.com/recipes/search", params=params)
    if r.status_code == 200:
        json_recipes = json.loads(r.content)
        recipes = json_recipes['results']
        return render_template('index.html', recipes=recipes)
