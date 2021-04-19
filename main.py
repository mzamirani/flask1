from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Open a new tab and enter /welcome/name for Url"
  
@app.route("/Welcome/<name>")
def Welcome_name(name):
  return "Welcome " + name + "!"

if __name__ == "__main__":
  app.run(debug=True)
