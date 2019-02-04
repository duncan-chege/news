from flask import render_template
from app import app
from .request import get_sources,get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources('mysources')
    print(news_sources)
   
    title= "Get the latest news"
    return render_template('index.html', title = title, sources = news_sources)

@app.route('/article/<article_id>')
def article(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('index.html',title = title, article = article)


