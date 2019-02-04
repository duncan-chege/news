import unittest
from app.models import article

Articles = article.Articles

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("cnbc",'CNBC','Stocks',"https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2017/10/24/104791816-GettyImages-856703910.1910x1000.jpg","Check out the companies","2019")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()