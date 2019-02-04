from app import app
import urllib.request,json
from .models import source

Sources = source.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(source):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v1/sources'.format(source,api_key)

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
        title = sources_item.get('title')
        description = sources_item.get('description')
        url = sources_item.get('url')
        content = sources_item.get('content')

        source_object= Sources(id, name, title, description,url,content)
        sources_results.append(source_object)

    return sources_results
