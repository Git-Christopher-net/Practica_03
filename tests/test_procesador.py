import unittest
import sys, os
sys.path.append(os.path.abspath("src"))

from procesador import Analizador


class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    # 1. Validar que el número de provincias sea coherente
    def test_numero_provincias_coherente(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIn("santa elena", resumen)
        self.assertIsInstance(resumen["santa elena"], float)
        self.assertGreater(resumen["santa elena"], 0)
    # 2. Verificar que los valores calculados sean numéricos y no negativos
    def test_valores_numericos_y_no_negativos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        for v in resumen.values():
            self.assertIsInstance(v, float)
            self.assertGreaterEqual(v, 0)

    # 3. Garantizar que la función retorne un diccionario
    def test_retorna_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    # 4. Verificar que las provincias consultadas existan
    def test_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    # 5. Provincia existente
    def test_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("pichincha")
        self.assertGreater(resultado, 0)

    # 6. Verificar valores correctos de 3 provincias (usa tus valores reales)
    def test_valores_especificos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIn("santa elena", resumen)
        self.assertIsInstance(resumen["santa elena"], float)
        self.assertGreater(resumen["santa elena"], 0)

    # =============================
    # ESTADÍSTICAS ADICIONALES
    # =============================

    def test_exportaciones_por_mes(self):
        exp = self.analizador.exportaciones_totales_por_mes()
        self.assertIn(9, exp)
        self.assertGreater(exp[9], 0)

    def test_porcentaje_tarifa_0(self):
        p = self.analizador.porcentaje_ventas_tarifa_0()
        self.assertIsInstance(p, dict)
        self.assertGreater(len(p), 10)

    def test_provincia_mayor_importaciones(self):
        prov, total = self.analizador.provincia_con_mayores_importaciones()
        self.assertIsInstance(prov, str)
        self.assertGreater(total, 0)
