import csv

class Analizador:

    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos, self.datos_raw = self._cargar_datos()

    def _cargar_datos(self):
        datos = []
        datos_raw = []

        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter="|")

            for fila in lector:
                datos_raw.append(fila.copy())

                provincia = fila["PROVINCIA"].strip().lower()

                ventas = float(fila["TOTAL_VENTAS"])

                datos.append({
                    "provincia": provincia,
                    "ventas": ventas
                })

        return datos, datos_raw

    # ----------------------------------------------------
    # 1️⃣ VENTAS TOTALES POR PROVINCIA
    # ----------------------------------------------------
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
            raise KeyError("Provincia no encontrada")
        return resumen[provincia]

    # ----------------------------------------------------
    # 2️⃣ EXPORTACIONES TOTALES POR MES
    # ----------------------------------------------------
    def exportaciones_totales_por_mes(self):
        resumen = {}
        for fila in self.datos_raw:
            mes = int(fila["MES"])
            export = float(fila["EXPORTACIONES"])
            resumen[mes] = resumen.get(mes, 0) + export
        return resumen

    # ----------------------------------------------------
    # 3️⃣ PORCENTAJE DE VENTAS TARIFA 0%
    # ----------------------------------------------------
    def porcentaje_ventas_tarifa_0(self):
        resultado = {}
        for fila in self.datos_raw:
            prov = fila["PROVINCIA"].lower()
            tarifa_0 = float(fila["VENTAS_NETAS_TARIFA_0"])
            total = float(fila["TOTAL_VENTAS"])

            if total > 0:
                porcentaje = (tarifa_0 / total) * 100
            else:
                porcentaje = 0

            resultado[prov] = resultado.get(prov, 0) + porcentaje

        return resultado

    # ----------------------------------------------------
    # 4️⃣ PROVINCIA CON MAYORES IMPORTACIONES
    # ----------------------------------------------------
    def provincia_con_mayores_importaciones(self):
        resumen = {}
        for fila in self.datos_raw:
            prov = fila["PROVINCIA"].lower()
            imp = float(fila["IMPORTACIONES"])
            resumen[prov] = resumen.get(prov, 0) + imp

        provincia_max = max(resumen, key=resumen.get)
        return provincia_max, resumen[provincia_max]
