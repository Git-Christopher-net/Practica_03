import csv

class Analizador:

    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            # tu archivo usa | como separador
            lector = csv.DictReader(archivo, delimiter="|")

            for fila in lector:
                # Provincia viene en la columna llamada "provincia"
                provincia = fila["provincia"].strip().lower()

                # La última columna es ventas
                # DictReader mantiene el orden original del archivo
                nombre_ultima_columna = list(fila.keys())[-1]
                venta = float(fila[nombre_ultima_columna])

                datos.append({"provincia": provincia, "ventas": venta})

        return datos

    def ventas_totales_por_provincia(self):
        resumen = {}
        for fila in self.datos:
            prov = fila["provincia"]
            resumen[prov] = resumen.get(prov, 0) + fila["ventas"]
        return resumen

    def ventas_por_provincia(self, provincia):
        provincia = provincia.lower()
        resumen = self.ventas_totales_por_provincia()

        if provincia not in resumen:
            raise KeyError(f"Provincia '{provincia}' no encontrada")

        return resumen[provincia]
