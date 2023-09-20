import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Roteador:
    def __init__(self, username, password, url_router, username_novo, password_novo):
        self.username = username
        self.password = password
        self.username_novo = username_novo
        self.password_novo = password_novo
        self.url_router = url_router

    def start_driver(self):
        self.driver = webdriver.Firefox()
        # self.driver.set_window_size(1024, 768)
        self.driver.get(self.url_router)
       

    def login_router(self):

        # Aguardar até que o campo de nome de usuário esteja presente
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-user"]'))
        )
        username_field.send_keys(self.username)

        # Aguardar até que o campo de senha esteja presente
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
        )
        password_field.send_keys(self.password)

        # Aguardar até que o botão de login esteja presente
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="button-login"]'))
        )
        login_button.click()
       

    def fechar_popup(self):

        try:
            
            # Aguarde até que o elemento do botão de fechamento da pop-up seja clicável
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-no"]'))
            )
            # Clique no botão de fechamento
            close_button.click()
            
        except Exception as e:
            pass
            
         # Entra em menu
            menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-button"]'))
                )
            menu_button.click()


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
            
            wireless_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ssid"]'))
            )
            wireless_button.send_keys(self.username_novo)

            scroll_pixels = 1000
            self.driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
            
            wireless_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="wireless-password"]'))
            )
            wireless_button.clear() 

            wireless_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="wireless-password"]'))
            )
            wireless_button.send_keys(self.password_novo)
          
            wireless_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="itb-input-icon-wireless-password"]'))
            )
            wireless_button.click() 

            wireless_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="button-save"]'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", wireless_button)
            wireless_button.click()

    def close_driver(self):
        if self.driver:
            self.driver.quit()

def start_automation():
    username = username_entry.get()
    password = password_entry.get()
    username_novo = novo_username.get()
    password_novo = novo_password.get()
    url_router =  'http://' + ip_rout_entry.get()

    rotbot = Roteador(username, password, url_router, username_novo, password_novo )
    rotbot.start_driver()
    rotbot.login_router()
    rotbot.fechar_popup()
    messagebox.showinfo("Informação", "Login bem-sucedido!, senha alterada com sucesso")
    rotbot.close_driver()


root = tk.Tk()
root.title("Configure o Roteador")
root.geometry("500x600")

# Container para centralizar os elementos
center_frame = tk.Frame(root)
center_frame.pack(expand=True, fill="both")


explanation_label = tk.Label(center_frame, text="Abaixo digite as credenciais do roteador so intelbras\n")
explanation_label.pack()

ip_rout = tk.Label(center_frame, text='digite o ip ex 10.0.0.1')
ip_rout.pack()

ip_rout_entry = tk.Entry(center_frame)
ip_rout_entry.pack()

# Cria campos de entrada para o usuário e senha
username_label = tk.Label(center_frame, text="Usuário:")
username_label.pack()

username_entry = tk.Entry(center_frame)
username_entry.pack()

password_label = tk.Label(center_frame, text="Senha:")
password_label.pack()

password_entry = tk.Entry(center_frame, show="*\n")
password_entry.pack()

# Espaço entre a segunda entrada e o texto explicativo
spacer_label = tk.Label(center_frame, text="")
spacer_label.pack()

explanation_label = tk.Label(center_frame, text="Abaixo troque usuario e senha do wifi\n")
explanation_label.pack()

username_ = tk.Label(center_frame, text="Novo usuario")
username_.pack()

novo_username = tk.Entry(center_frame)
novo_username.pack()

password_ = tk.Label(center_frame, text="Nova senha")
password_.pack()

novo_password = tk.Entry(center_frame, show='*')
novo_password.pack()

spacer_label = tk.Label(center_frame, text="")
spacer_label.pack()

# Botão para iniciar o processo de automação
login_button = tk.Button(center_frame, text="Iniciar Automação", command=start_automation)
login_button.pack()

# Centralizar o container na janela
center_frame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
