import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Roteador:
    def __init__(self, username, password, url_router, username_novo, password_novo):
        self.username = username
        self.password = password
        self.username_novo = username_novo
        self.password_novo = password_novo
        self.url_router = url_router

    def start_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url_router)

    def login_router(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-user"]'))
        )
        username_field.send_keys(self.username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
        )
        password_field.send_keys(self.password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="button-login"]'))
        )
        login_button.click()

    def fechar_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-no"]'))
            )
            close_button.click()
            
        except Exception as e:
            pass

    def entrar_menu(self):
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-button"]'))
            )
        menu_button.click()

    def alterar_configuracoes_wifi(self):
        menu_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-networks"]'))
            )
        menu_click.click()

        wifi_action = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wifi-ssid-action-0"]'))
        )
        wifi_action.click()

        wireless_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ssid"]'))
        )
        wireless_button.clear()
        
        wireless_button.send_keys(self.username_novo)

        scroll_pixels = 1000
        self.driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
        
        wireless_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wireless-password"]'))
        )
        wireless_button.clear() 

        wireless_button.send_keys(self.password_novo)
      
    def finalizar_configuracao_wifi(self):
        wireless_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="itb-input-icon-wireless-password"]'))
        )

def start_automation():
    # Aqui você pode chamar as funções de configuração com base na opção selecionada pelo usuário
    selected_option = option_var.get()
    if selected_option == "Configuração 1":
        # Chame a função para a Configuração 1
        pass
    elif selected_option == "Configuração 2":
        # Chame a função para a Configuração 2
        pass
    else:
        # Trate outros casos
        pass

root = tk.Tk()
root.title("Configure o Roteador")

# Crie uma variável StringVar para armazenar a opção selecionada pelo usuário
option_var = tk.StringVar()

# Crie os botões de opção
option1 = tk.Radiobutton(root, text="Configuração 1", variable=option_var, value="Configuração 1")
option1.pack()

option2 = tk.Radiobutton(root, text="Configuração 2", variable=option_var, value="Configuração 2")
option2.pack()

# Botão para iniciar o processo de automação
login_button = tk.Button(root, text="Iniciar Automação", command=start_automation)
login_button.pack()

root.mainloop()