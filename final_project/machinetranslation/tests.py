import unittest
# Juan Marrugo
from translator import frenchToEnglish, englishToFrench

class Testfr_en(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Monde'), 'Mundo')

class Testfr_en(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('World'), 'Mundo')

unittest.main()