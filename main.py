from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/recipes/')
def recipes():
  return render_template('recipes.html')


@app.route('/recipe_1/')
def recipe_1():
  return render_template('recipe_1.html')


@app.route('/about/')
def about():
  return render_template('about.html')


@app.route('/contact/')
def contact():
  return render_template('contact.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
