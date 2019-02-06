import unittest
from  app.models import Sources


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("foxnews",'Fox News','Joaqin Guzman is dangerous',"https://www.foxnews.com/us/el-chapo-accused-of-drugging-rapping-girls-as-young-as-13-in-court-documents")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
