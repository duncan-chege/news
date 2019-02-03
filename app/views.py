from flask import render_template
from app import app
from .request import get_manynews

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_news = get_manynews('business')
    print(business_news)
    title= "Get the latest news"
    return render_template('index.html', title = title, business = business_news)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the mnews details page and its data
    '''
    return render_template('news.html',id = news_id)


