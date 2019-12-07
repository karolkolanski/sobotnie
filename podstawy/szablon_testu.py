import unittest

class MojScenariuszTestowy(unittest.TestCase):
    """Scenariusz testowy"""
    def setUp(self) -> None:
        """Przygotowania przed każdym testem"""
        pass
    """
    Poniżej metody rozpoczynające się od słowa
    test. Są to właściwe testy 
    """
    def testPierwszy(self):
        pass
    def testDrugi(self):
        pass
    # i tak dalej...
    def tearDown(self) -> None:
        """Sprzątanie po każdym teście"""
        pass