import unittest

from veiculo import veiculo
"""
(self, marca, modelo, dono, tanque_capacid,tanque_atual, autonomia_km_l, km_rodados)
"""

class TestVeiculo(unittest.TestCase):
    def test_lerTanqueAtual(self):
        car1 = veiculo('Fiat','Siena','Carlos',80,0,5,0)
        self.assertEqual(car1.lerTanqueAtual(),0)

if __name__ == "__main__":
    unittest.main()