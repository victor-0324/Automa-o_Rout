import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Roteador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configure o Roteador")
        self.root.geometry("500x600")

        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        # Frame para a primeira página
        self.page1_frame = tk.Frame(self.main_frame)

        # Frame para a segunda página
        self.page2_frame = tk.Frame(self.main_frame)

        # Variável de controle para a opção selecionada
        self.option_var = tk.StringVar()

        # Quadro da página atual
        self.current_page = None

        # Botões de seleção
        option1 = tk.Radiobutton(self.page1_frame, text="Configurar Wifi?", variable=self.option_var, value="Configuração 1")
        option1.pack()

        option2 = tk.Radiobutton(self.page1_frame, text="Configuração 2", variable=self.option_var, value="Configuração 2")
        option2.pack()

        # Botão para iniciar o processo de escolha
        login_button = tk.Button(self.page1_frame, text="digitar informações", command=self.config_fild)
        login_button.pack()

        # Espaçador
        spacer_label = tk.Label(self.page1_frame, text="")
        spacer_label.pack()

        self.explanation_label = tk.Label(self.page1_frame, text="")
        self.explanation_label.pack()

        # Centralizar o frame da página atual na janela
        self.page1_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.root.mainloop()

    def config_fild(self):
        selected_option = self.option_var.get()
        
        if selected_option == "Configuração 1":
            self.show_page1()
            self.explanation_label.config(text="Abaixo digite as credenciais do roteador so intelbras")
            self.create_page1_fields()

        elif selected_option == "Configuração 2":
            self.show_page2()
            self.explanation_label.config(text="Abaixo digite outras configurações")
            self.create_page2_fields()
            
        else:
            self.destroy_page1_fields()
            self.destroy_page2_fields()
            self.explanation_label.config(text="")

    def show_page1(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.page1_frame
        self.page1_frame.pack()

    def show_page2(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.page2_frame
        self.page2_frame.pack()

    def create_page1_fields(self):
        # Implemente os campos da página 1 aqui
        pass

    def create_page2_fields(self):
        # Implemente os campos da página 2 aqui
        pass

    def destroy_page1_fields(self):
        # Implemente a destruição dos campos da página 1 aqui
        pass

    def destroy_page2_fields(self):
        # Implemente a destruição dos campos da página 2 aqui
        pass

if __name__ == "__main__":
    Roteador()
