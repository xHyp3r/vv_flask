from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return " <a href='/home'>Hi!</a>"

@app.route('/about')
def about():
  return render_template('about.html',)

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 81449303)

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/params')
def params():
  return render_template('params.html', args = request.args.to_dict())

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)