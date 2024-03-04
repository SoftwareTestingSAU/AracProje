import unittest
from AracProje.mymodels.Arac import Arac

class AracTest(unittest.TestCase):
    def test_valid_form(self):
        veri = {
            'hiz': 120,
            'zaman': 2,
            'depo': 48
        }
        arac = Arac(data=veri)
        self.assertTrue(arac.is_valid())

    def test_invalid_form(self):
        # Test an invalid form (missing required field)
        veri = {
            'hiz': 120,
            'zaman': 2
        }
        arac = Arac(data=veri)
        self.assertFalse(arac.is_valid())

    def test_menzil(self):
        veri = {
            'hiz': 120,
            'zaman': 2,
            'depo': 48
        }
        arac = Arac(data=veri)
        self.assertEqual(arac.menzil(),600)

        
if __name__ == '__main__':
    unittest.main()
