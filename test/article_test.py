import unittest
from app.models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("cnbc",'CNBC','Stocks',"https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2017/10/24/104791816-GettyImages-856703910.1910x1000.jpg","Check out the companies","2019","a date")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
