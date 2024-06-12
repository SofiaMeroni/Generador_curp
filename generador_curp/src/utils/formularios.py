from selenium.webdriver.common.by import By

def llenado_de_formulario(driver, value, input):
    # Esto completa campos de formularios buscando By.NAME y siendo
    # el nombre un valor (value) y escribe en el campo lo que
    # esta en la variable input
    input_text_fname = driver.find_element(By.NAME, value)
    input_text_fname.send_keys(input)