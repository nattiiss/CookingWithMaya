from flask import Flask, render_template, jsonify

app = Flask(__name__)

Cakes = [{
  'id': 1,
  'title': 'cake1',
  'recipe': 'recipe 1'
}, {
  'id': 2,
  'title': 'cake2',
  'recipe': 'recipe 2'
}, {
  'id': 3,
  'title': 'cake3',
  'recipe': 'recipe 3'
}]


@app.route("/")
def hello_world():
  return render_template('index.html', cakes=Cakes)


@app.route("/api/cakes")
def list_cake():
  return jsonify(Cakes)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


