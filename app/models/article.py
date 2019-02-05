class Articles:
    '''
    article class to define article Objects
    '''

    def __init__(self,id,name,title,urlToImage,content,publishedAt):
        self.id =id
        self.name = name
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt