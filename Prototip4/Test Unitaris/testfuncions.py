import unittest

# Funcions a provar
def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b

def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

# Classe de test
class TestFuncions(unittest.TestCase):
    # Tests per a la funció suma
    def test_suma_positius(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negatius(self):
        self.assertNotEqual(suma(-2, -3), -7)

    def test_suma_mixt(self):
        self.assertGreater(suma(-2, 3), 0)

    # Tests per a la funció resta
    def test_resta_positius(self):
        self.assertEqual(resta(5, 3), 2)

    def test_resta_negatius(self):
        self.assertEqual(resta(-5, -3), -2)

    def test_resta_mixt(self):
        self.assertLess(resta(-5, 3), 0)

    # Tests per a la funció divideix
    def test_divideix_positius(self):
        self.assertEqual(divideix(6, 3), 2)

    def test_divideix_negatius(self):
        self.assertEqual(divideix(-6, -3), 2)

    def test_divideix_mixt(self):
        self.assertLess(divideix(-6, 3), 0)

    def test_divideix_per_zero(self):
        self.assertEqual(divideix(6, 0), "Error: divisió per zero")

    def test_divideix_tipus(self):
        self.assertIsInstance(divideix(6, 3), float)

# Executar els tests
if __name__ == "__main__":
    unittest.main()