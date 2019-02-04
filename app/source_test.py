import unittest
from  app.models import source

Sources = source.Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("fox-news",'Fox News','El-chapo','Joaqin Guzman is dangerous',"https://www.foxnews.com/us/el-chapo-accused-of-drugging-rapping-girls-as-young-as-13-in-court-documents","The accusations are disturbing")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()