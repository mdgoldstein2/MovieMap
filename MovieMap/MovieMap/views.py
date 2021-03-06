"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MovieMap import app
from access import getMovie

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='About Movie Map.'
    )

@app.route('/test')
def test():
    """Renders a test page."""
    return render_template(
        'test.html',
        title='Test',
        year=datetime.now().year,
        message='Your application test page.',
        success = getMovie(500)
    )

