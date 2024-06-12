from selenium import webdriver
#from selenium.webdriver.edge.service import Service
from src.paginas import generador_curp_rfc
import time
import json

# Comienzo del reloj
comienzo = time.time()

driver = webdriver.Firefox()
driver.maximize_window()
print("El programa se inició")

# Inicio de Sesión
generador_curp_rfc.curp_rfc(driver)

with open ('generador_curp\src\datos\curps.json') as curps:
    datos = json.load(curps)

# Obtener la lista de CURPs
curps_lista = datos.get('id_curp', [])


driver.quit()
print("El programa se cerró")

# Finalización del reloj
final = time.time()
tiempo_total = final - comienzo
print(tiempo_total)