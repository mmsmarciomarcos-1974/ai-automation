import unittest
import sys
import os

# Adiciona a pasta 'src' ao caminho para o Python encontrar o módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculo_bonus import calcular_bonus_fidelidade

class TestBonusCobolRule(unittest.TestCase):

    def test_bonus_veterano_15_porcento(self):
        # Cenário: Salário 1000, 11 anos de casa. Esperado: 150.00
        resultado = calcular_bonus_fidelidade(1000.00, 11)
        self.assertEqual(resultado, 150.00)

    def test_bonus_pleno_10_porcento(self):
        # Cenário: Salário 1000, 6 anos de casa. Esperado: 100.00
        resultado = calcular_bonus_fidelidade(1000.00, 6)
        self.assertEqual(resultado, 100.00)

    def test_bonus_junior_5_porcento(self):
        # Cenário: Salário 1000, 2 anos de casa. Esperado: 50.00
        resultado = calcular_bonus_fidelidade(1000.00, 2)
        self.assertEqual(resultado, 50.00)

if __name__ == '__main__':
    unittest.main()