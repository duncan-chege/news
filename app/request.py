from app import app
import urllib.request,json
from .models import source,article

Sources = source.Sources
Articles = article.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

base2_url = app.config["ARTICLE_API_BASE_URL"]

def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')


        source_object= Sources(id, name, description,url)
        sources_results.append(source_object)

    return sources_results

def get_article(articles):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base2_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):

    '''
    Function  that processes the articles result and transform them to a list of articles

    Args:
        articles_list: A list of dictionaries that contain articles

    Returns :
        articles_results: A list of article objects
    ''' 
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        title = articles_item.get('title')
        urlToImage = articles_item.get('urlToImage')
        content = articles_item.get('content')
        publishedAt = articles_item.get('publishedAt')


    article_object= Articles(id, name, title, urlToImage, content, publishedAt)
    articles_results.append(article_object)

    return articles_results

# def get_article(id):
#     get_article_details_url = base2_url.format(api_key)

#     with urllib.request.urlopen(get_article_details_url) as url:
#         article_details_data = url.read()
#         article_details_response = json.loads(article_details_data)

#         article_object = None

#         if article_details_response:
#             id = article_details_response.get('id')
#             name = article_details_response.get('name')
#             title = article_details_response.get('title')
#             urlToImage = article_details_response.get('urlToImage')
#             content = article_details_response.get('content')
#             publishedAt = article_details_response.get('publishedAt')

#             article_object = Articles(id,name,title,urlToImage,content,publishedAt)

#     return article_object
