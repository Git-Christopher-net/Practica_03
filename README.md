# Práctica 03 – Calidad de Software

## 📌 Descripción
Proyecto que analiza un archivo CSV del SRI y aplica pruebas unitarias con `unittest`.  
También se calcula la cobertura de código usando la librería `coverage`.

---

## 🧪 Pruebas Unitarias
Para ejecutar los tests:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
coverage run -m unittest discover -s tests -p "test_*.py"
coverage report
Name                     Stmts   Miss  Cover
--------------------------------------------
src/procesador.py          85      5    94%
practica-03/
│── app.py
│── README.md
│── .gitignore
│── datos/
│── src/
│── tests/
│── venv/
