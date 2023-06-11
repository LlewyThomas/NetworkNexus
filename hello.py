from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Create route decorator
@app.route('/')

def index():
    list = ["item1","item2","last_item"]
    return render_template("index.html", list=list)

# create person route
@app.route('/person/<name>')

def person(name):
    return render_template("person.html",person_name=name) 


# Invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html") , 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html") , 500