import unittest

# Funció a provar
def suma(a, b):
    return a + b

# Classe de test
class TestSuma(unittest.TestCase):
    def test_suma_positius(self):
        self.assertEqual(suma(2, 3), 5)  # Comprova que 2 + 3 = 5

    """def test_suma_inccorecte(self):
        self.assertEqual(suma(2, 3), 6)  # Què passa si falla el test?"""

    def test_suma_negatius(self):
        self.assertNotEqual(suma(-2, -3), -7)  # Comprova que -2 + -3 =/= -7

    def test_suma_mixt(self):
        self.assertGreater(suma(-2, 3), 0)  # Comprova que -2 + 3 > 0

    def test_suma_zero(self):
        self.assertIsInstance(suma(0, 5), int)  # Comprova que el resultat és un enter

    def test_suma_gran(self):
        self.assertLess(suma(100, 200), 500)  # Comprova que 100 + 200 < 500

    def test_suma_none(self):
        self.assertIsNotNone(suma(1, 1))  # Comprova que el resultat no és None

# Executar els tests
if __name__ == "__main__":
    unittest.main()