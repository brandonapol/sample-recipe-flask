from flask import Flask, render_template
from dict import recipes

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
#   comment out one of the two lines following
#   return 'Hello, World!'
  return render_template('actual_index.html')

@app.route('/list')
def recipe_list():
    return render_template('recipe_page.html', recipe_id = recipes)

@app.route('/recipe/<int:recipe_number>')
# @app.route('/recipe')
def recipe(recipe_number):
    return render_template('index.html', recipe_id = recipes[recipe_number])