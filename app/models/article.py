class Articles:
    '''
    article class to define article Objects
    '''

    def __init__(self,id,name,title,url,urlToImage,content,publishedAt):
        self.id =id
        self.name = name
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt