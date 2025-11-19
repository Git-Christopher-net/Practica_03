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
                fila_normalizada = {k: v.strip() for k, v in fila.items()}
                datos_raw.append(fila_normalizada)

                # datos simplificados
                provincia = fila_normalizada["PROVINCIA"].lower()
                ventas = float(fila_normalizada["TOTAL_VENTAS"])

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
        for fila in self.datos:     #  <--- CORRECTO (usa datos simplificados)
            prov = fila["provincia"]
            resumen[prov] = resumen.get(prov, 0) + fila["ventas"]
        return resumen

    def ventas_por_provincia(self, provincia):
        provincia = provincia.strip().lower()
        resumen = self.ventas_totales_por_provincia()

        if provincia not in resumen:
            raise KeyError("Provincia no encontrada")
        return resumen[provincia]

    # ----------------------------------------------------
    # 2️⃣ EXPORTACIONES TOTALES POR MES
    # ----------------------------------------------------
    def exportaciones_totales_por_mes(self):
        resumen = {}
        for fila in self.datos_raw:    #  <--- AHORA CORRECTO
            mes = int(fila["MES"])
            export = float(fila["EXPORTACIONES"])
            resumen[mes] = resumen.get(mes, 0) + export
        return resumen

    # ----------------------------------------------------
    # 3️⃣ PORCENTAJE PROMEDIO DE TARIFA 0%
    # ----------------------------------------------------
    def porcentaje_ventas_tarifa_0(self):
        acumulado = {}
        contador = {}

        for fila in self.datos_raw:   #  <--- AHORA CORRECTO
            prov = fila["PROVINCIA"].lower()

            tarifa_0 = float(fila["VENTAS_NETAS_TARIFA_0"])
            total = float(fila["TOTAL_VENTAS"])

            porcentaje = (tarifa_0 / total) * 100 if total > 0 else 0

            acumulado[prov] = acumulado.get(prov, 0) + porcentaje
            contador[prov] = contador.get(prov, 0) + 1

        return {p: acumulado[p] / contador[p] for p in acumulado}

    # ----------------------------------------------------
    # 4️⃣ PROVINCIA CON MAYORES IMPORTACIONES
    # ----------------------------------------------------
    def provincia_con_mayores_importaciones(self):
        resumen = {}

        for fila in self.datos_raw:   #  <--- AHORA CORRECTO
            prov = fila["PROVINCIA"].lower()
            imp = float(fila["IMPORTACIONES"])
            resumen[prov] = resumen.get(prov, 0) + imp

        provincia_max = max(resumen, key=resumen.get)
        return provincia_max, resumen[provincia_max]
