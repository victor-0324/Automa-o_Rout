import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

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
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-no"]'))
            )
            # Clique no botão de fechamento
            close_button.click()
            
        except Exception as e:
            pass
            
    def alterar_configuracoes_wifi(self):
            
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
                EC.element_to_be_clickable((By.XPATH, '//*[@id="wifi-ssid-action-1"]'))
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

    def alterar_config_rout(self):
            #  Entra em menu
             # Entra em menu
            menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-button"]'))
                )
            menu_button.click()


            menu_button  = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="menu-system"]'))
            )
            self.driver.execute_script("arguments[0].click();", menu_button )
            
            menu_button  = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="menu-system-user"]'))
            )
            self.driver.execute_script("arguments[0].click();", menu_button )

            menu_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
            )
            menu_button.send_keys(self.username_novo)

            menu_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
            )
            menu_button.send_keys(self.password_novo)

            menu_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="confirmation"]'))
            )
            menu_button.send_keys(self.password_novo)

            menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="button-save-user"]'))
            )
            self.driver.execute_script("arguments[0].click();", menu_button )

    def close_driver(self):
        if self.driver:
            self.driver.quit()


# TELA TKINTER PARA O USUARIO
class Roteador_tk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configure o Roteador")
        self.root.geometry("500x500")

        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        # Frame para a primeira página
        self.page1_frame = tk.Frame(self.main_frame)

        # Frame para a segunda página
        self.page2_frame = tk.Frame(self.main_frame)

        # Frame para a terceira pagina
        self.page3_frame = tk.Frame(self.main_frame)

        # Variável de controle para a opção selecionada
        self.option_var = tk.StringVar()

        # Quadro da página atual
        self.current_page = None

        explanation_label = tk.Label(self.page1_frame, text="Abaixo escolha a opção para configurar seu roteador\n")
        explanation_label.pack()

        # Crie os botões de opção
        option1 = tk.Radiobutton(self.page1_frame, text="Trocar nome e senha do WI-FI", variable=self.option_var, value="Configuração 1")
        option1.pack()

         # Espaçador
        self.spacer_label = tk.Label(self.page1_frame, text="")
        self.spacer_label.pack()

        option2 = tk.Radiobutton(self.page1_frame, text="Troca senha do ROTEADOR", variable=self.option_var, value="Configuração 2")
        option2.pack()

        # Espaçador
        self.spacer_label = tk.Label(self.page1_frame, text="")
        self.spacer_label.pack()

        # Botão para iniciar o processo de escolha
        self.login_button = tk.Button(self.page1_frame, text="Configurar", command=self.config_fild)
        self.login_button.pack()

        # Espaçador
        self.spacer_label = tk.Label(self.page1_frame, text="")
        self.spacer_label.pack()

        self.explanation_label = tk.Label( text="")
        self.explanation_label.pack()

         # Centralizar o container na janela
        self.page1_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.root.mainloop()

    def show_page2(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.page2_frame
        self.page2_frame.pack()

    def show_page3(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.page3_frame
        self.page3_frame.pack()

    def config_fild(self):
        selected_option = self.option_var.get()
        if selected_option == "Configuração 1":
            self.show_page2()
            self.create_page2_fields()
            self.destroy_page1_fields()

        elif selected_option == "Configuração 2":
            self.show_page3()
            self.create_page3_fields()
            self.destroy_page2_fields()

    def destroy_page1_fields(self):
        # Implementa a destruição da pagina 1
        # self.login_button.destroy()
        self.page1_frame.destroy()
        pass

    def destroy_page2_fields(self):
        # Implementa a destruição da pagina 1
        # self.page1_frame.destroy()
        self.page2_frame.destroy()
        pass

    def create_page2_fields(self):
        self.page2_frame.place(relx=0.5, rely=0.5, anchor="center")
        explanation_label = tk.Label(self.page2_frame, text="Abaixo digite as credenciais do seu roteador\n")
        explanation_label.pack()

        self.ip_rout = tk.Label(self.page2_frame, text='digite o ip Ex: 10.0.0.1')
        self.ip_rout.pack()

        self.ip_rout_entry = tk.Entry(self.page2_frame)
        self.ip_rout_entry.pack()

        # Cria campos de entrada para o usuário e senha
        username_label = tk.Label(self.page2_frame, text="Usuário:")
        username_label.pack()

        self.username_entry = tk.Entry(self.page2_frame)
        self.username_entry.pack()

        password_label = tk.Label(self.page2_frame, text="Senha:")
        password_label.pack()

        self.password_entry = tk.Entry(self.page2_frame, show="*\n")
        self.password_entry.pack()

        # Espaço entre a segunda entrada e o texto explicativo
        spacer_label = tk.Label(self.page2_frame, text="")
        spacer_label.pack()

        explanation_label = tk.Label(self.page2_frame, text="Abaixo troque usuario e senha do WI-FI\n")
        explanation_label.pack()

        username_ = tk.Label(self.page2_frame, text="Novo usuario")
        username_.pack()

        self.novo_username = tk.Entry(self.page2_frame)
        self.novo_username.pack()

        password_ = tk.Label(self.page2_frame, text="Nova senha")
        password_.pack()

        self.novo_password = tk.Entry(self.page2_frame, show='*')
        self.novo_password.pack()

        spacer_label = tk.Label(self.page2_frame, text="")
        spacer_label.pack()

        # Botão para iniciar o processo de automação
        self.login_button = tk.Button(self.page2_frame, text="Iniciar Automação", command=self.start_automation)
        self.login_button.pack() 
    
    def validate_password_strength(self, event):
        password = self.senha_rout_entry.get()
        if self.is_strong_password(password):
            # Senha forte, ative o botão
            self.login_button_3['state'] = tk.NORMAL
        else:
            # Senha fraca, desative o botão
            self.login_button_3['state'] = tk.DISABLED

    def is_strong_password(self, password):
        # Verifique se a senha atende aos requisitos: Minúscula, Maiúscula, Número, Símbolo, Mínimo de 8 caracteres
        if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*]', password) and len(password) >= 8:
            return True
        else:
            return False

    def create_page3_fields(self):
        self.page3_frame.place(relx=0.5, rely=0.5, anchor="center")
        explanation_label = tk.Label(self.page3_frame, text="Abaixo digite as novas credenciais do seu roteador\n")
        explanation_label.pack() 

        self.ip_rout = tk.Label(self.page3_frame, text='digite o ip ex 10.0.0.1')
        self.ip_rout.pack()

        self.ip_rout_entry = tk.Entry(self.page3_frame)
        self.ip_rout_entry.pack()

        # Cria campos de entrada para o usuário e senha
        username_label = tk.Label(self.page3_frame, text="Usuário:")
        username_label.pack()

        self.username_entry = tk.Entry(self.page3_frame)
        self.username_entry.pack()

        password_label = tk.Label(self.page3_frame, text="Senha:")
        password_label.pack()

        self.password_entry = tk.Entry(self.page3_frame, show="*\n")
        self.password_entry.pack()

        # Espaçador
        self.spacer_label = tk.Label(self.page3_frame, text="")
        self.spacer_label.pack()

        explanation_label = tk.Label(self.page3_frame, text="Abaixo Defina as credenciais para acesso às configurações do ROTEADOR\nMinúscula, Maiúscula, Número, Símbolo, Mínimo de 8 caracteres\n")
        explanation_label.pack()

        self.user_rout = tk.Label(self.page3_frame, text='Digite o novo usuario')
        self.user_rout.pack()

        self.user_rout_entry = tk.Entry(self.page3_frame)
        self.user_rout_entry.pack()

        # Espaçador
        self.spacer_label = tk.Label(self.page3_frame, text="")
        self.spacer_label.pack()

        self.senha_rout = tk.Label(self.page3_frame, text='Digite a nova senha')
        self.senha_rout.pack()

        self.senha_rout_entry = tk.Entry(self.page3_frame)
        self.senha_rout_entry.pack()

        # Espaçador
        self.spacer_label = tk.Label(self.page3_frame, text="")
        self.spacer_label.pack()

        # Botão para iniciar o processo de automação
        self.login_button_3 = tk.Button(self.page3_frame, text="Iniciar Automação", command=self.start_troca_senha)
        self.login_button_3.pack() 

        # Associe a função de validação à entrada de senha
        # self.senha_rout_entry.bind("<KeyRelease>", self.validate_password_strength)

    def start_automation(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        username_novo = self.novo_username.get()
        password_novo = self.novo_password.get()
        url_router =  'http://' + self.ip_rout_entry.get()
        rotbot = Roteador(username, password, url_router, username_novo, password_novo )

        rotbot.start_driver()
        rotbot.login_router()
        rotbot.fechar_popup()
        rotbot.alterar_configuracoes_wifi()
        messagebox.showinfo("Informação", "Login bem-sucedido!, senha alterada com sucesso")
        rotbot.close_driver()

    def start_troca_senha(self):
        password = self.senha_rout_entry.get()
        if not self.is_strong_password(password):
            # Senha fraca, mostre uma mensagem de erro ou realize outra ação adequada
            messagebox.showinfo("SENHA FRACA"," Por favor escolha uma senha forte.")
            return
        
        username = self.username_entry.get()
        password = self.password_entry.get()
        username_novo = self.user_rout_entry.get()
        password_novo = self.senha_rout_entry.get()
        url_router =  'http://' + self.ip_rout_entry.get()
        rotbot = Roteador(username, password, url_router, username_novo, password_novo )
            
        rotbot.start_driver()
        rotbot.login_router()
        rotbot.fechar_popup()
        rotbot.alterar_config_rout()
        messagebox.showinfo("Informação", "Login bem-sucedido!, senha alterada com sucesso")
        rotbot.close_driver()

if __name__ == "__main__":
    Roteador_tk()
