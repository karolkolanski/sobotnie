import unittest

class MojPrzypadekTetsowy(unittest.TestCase):
    """
    Przypadek testowy
    """
    def setUp(self):
        # Przygotowanie do testu
        # (Warunki wstępne)
        print("Przygotowanie do testu...")

    def testGoogleSearch(self):
        # Właściwy test
        print("tutaj będziemy coś testować")

    def test2(self):
        print("Test drugi")

    def test3(self):
        print("Test trzeci")

    def tearDown(self):
        # Sprzątanie po teście
        print("Test zakończony. sprzątamy")

if(__name__ == '__main__'):
    unittest.main()
