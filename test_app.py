"""# tests/test_app.py
import sys
from joblib import load
import unittest


from main import classify_text #Importing classify Function from main.py file
from dummy_model import DummyModel

class MyAppTestCase(unittest.TestCase):
    def test_classify_text():
        model = load('spam_model.joblib')

        assert classify_text("You've won a prize!", model) == "Spam"
        #Python's assert statement allows you to write sanity checks in your code. 
        #It will pass this statement if is it spam then it will pass otherwise throw error
        
        assert classify_text("Hello, how are you?", model) == "Not Spam"

    test_classify_text()

"""

import sys
from joblib import load
import unittest

from main import classify_text #Importing classify Function from main.py file
from dummy_model import DummyModel

class MyAppTestCase(unittest.TestCase):
    def test_classify_text(self):    # 'self' needs to be included here
        model = load('spam_model.joblib')

        self.assertEqual(classify_text("You've won a prize!", model), "Spam")
        self.assertEqual(classify_text("Hello, how are you won?", model), "Not Spam")

#if __name__ == '__main__':
 #   unittest.main()
