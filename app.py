from flask import Flask, render_template
import feedparser
from pygooglenews import GoogleNews
import json
app = Flask('app')

@app.route('/')
def index():
    gn = GoogleNews()
    test = gn.top_news()
    entries = test['entries']
    main_post = entries[0]
    posts = entries[1:10]
    return render_template('index.html', posts=posts)

@app.route('/current-events')
def current():
    gn = GoogleNews()
    test = gn.search('current events')
    entries = test['entries']
    posts = entries[0:10]
    return render_template('current-events.html', posts=posts)

@app.route('/tech-news')
def tech():
    gn = GoogleNews()
    test = gn.search('tech')
    entries = test['entries']
    posts = entries[0:10]
    return render_template('tech-news.html', posts=posts)


@app.route('/stocks')
def stocks():
    gn = GoogleNews()
    test = gn.search('stocks')
    entries = test['entries']
    posts = entries[0:10]
    return render_template('stocks.html', posts=posts)

@app.route('/bay-area')
def bay_area():
    gn = GoogleNews()
    test = gn.geo_headlines('bay area')
    entries = test['entries']
    posts = entries[0:10]
    return render_template('bay-area.html', posts=posts)

