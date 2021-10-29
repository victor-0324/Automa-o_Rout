#usr/bin/python3.8
from sys import _clear_type_cache
from selenium import webdriver
from time import sleep
from datetime import date, datetime
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import keyboard


username = 'admin'
password = 'SuaSenha'
Url_rout = 'http://10.0.0.1/#/login'
novo = 'NOVASENHA123'

class Roteador:
    def __init__(self,username ,password, Url_rout, ):
        self.username = username
        self.password = password 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(1024, 1180)
        #self.driver.set_window_position(400, 50)
        self.driver.get(Url_rout)
        sleep(5)

        #
        senha  = self.driver.find_element_by_xpath("//*[@id='login-user']")
        senha.send_keys(username)
        sleep(2)

        passwd = self.driver.find_element_by_xpath('//*[@id="login-password"]')
        passwd.send_keys(password)       
        sleep(3)

        #entra no roteador
        botao  = self.driver.find_element_by_xpath('//*[@id="button-login"]')
        botao.click()
        sleep(5)

        #botao do menu
        botao1 = self.driver.find_element_by_xpath('//*[@id="menu-button"]')
        botao1.click()
        sleep(3)

        #Entra em redes
        botao2 = self.driver.find_element_by_xpath('//*[@id="menu-networks"]/div')
        botao2.click()
        sleep(3)

        #trocar a senha
        botao3 = self.driver.find_element_by_xpath('//*[@id="wifi-ssid-action-1"]/div') 
        botao3.click()
        
        #apaga senha antiga
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        botao5 = self.driver.find_element_by_xpath('//*[@id="wireless-password"]')   
        botao5.click() 
        keyboard.press_and_release('Ctrl + A + Del')
        sleep(3)

        #escrever nova senha
        botao4 = self.driver.find_element_by_xpath('//*[@id="wireless-password"]') 
        botao4.send_keys(novo)
        sleep(3)

        salve = self.driver.find_element_by_xpath('//*[@id="button-save"]')
        salve.click()
        #keyboard.press_and_release('shift + Enter')
        sleep(10)
        
try:
    rotbot = Roteador(username, password, Url_rout)
    print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{username}] [{password}]Closing window...")
    rotbot.driver.close()
except:
    print("Fail")


    
        


