import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("fox-news",'Fox News','El-chapo','Joaqin Guzman is dangerous',"https://www.foxnews.com/us/el-chapo-accused-of-drugging-rapping-girls-as-young-as-13-in-court-documents","The accusations are disturbing")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()