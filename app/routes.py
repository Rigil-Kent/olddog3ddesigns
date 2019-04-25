from app import app
from app.forms import ContactForm
from flask import render_template, url_for


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/services/consumer-small-business')
def consumer():
    return render_template("consumer.html")

@app.route('/services/corporate')
def corporate():
    return render_template("corporate.html")

@app.route('/services/education')
def education():
    return render_template("education.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact')
def contact():

    form = ContactForm()

    return render_template('contact.html', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.html')