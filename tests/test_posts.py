import unittest
from app.models import Post

class PitchTest(unittest.TestCase):
    
    """
    Test class to test the behaviour of the Post
    """
    def setUp(self):
    
        """
        Set up method that will run before every Test
        """
        self.new_post= Post(1234, 'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post))
        