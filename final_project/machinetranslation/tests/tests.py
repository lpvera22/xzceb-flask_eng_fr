import unittest
from machinetranslation.translator import english_to_french, french_to_english

class VerificartranslateTests(unittest.TestCase):
    def test_null_frenchToEnglish(self):
        res = french_to_english(None)
        self.assertEqual(None, res)
    
    def test_null_englishToFrench(self):
        res = english_to_french(None)
        self.assertEqual(None, res)

    def test_text_frenchToEnglish(self):
        res = french_to_english('Bonjour')
        self.assertEqual('Hello', res)
    
    def test_text_englishToFrench(self):
        res = english_to_french('Hello')
        self.assertEqual('Bonjour', res)

