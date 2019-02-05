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
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(article_id)
    title = f'{article_id}'

    return render_template('article.html',title = title, myarticle = article, name=article_id)


