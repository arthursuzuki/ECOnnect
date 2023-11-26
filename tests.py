from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class SeuTeste(TestCase):
    def setUp(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.get('http://127.0.0.1:8000/')
        time.sleep(2)

    def test_Adicionando_EmpresaProx(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[4]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/button[1]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/form/p[1]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/form/p[2]/input').send_keys('testando')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/form/button').click()
        self.assertIn("teste", self.navegador.page_source)

    def test_ProcurandoPorCEP_EmpresaProx(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[4]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/input').send_keys('52171045')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/button[2]').click()
        time.sleep(1)
        cep = self.navegador.find_element(By.XPATH, '/html/body/div[2]/input').get_attribute("value")
        emp = self.navegador.find_element(By.XPATH, "/html/body/div[2]/div[2]")
        assert cep == "52171045" and emp is not None

    def test_RemovendoOCEP_EmpresaProx(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[4]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/input').send_keys('32156045')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/button[2]').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/input').clear()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/button[2]').click()
        time.sleep(1)
        cep = self.navegador.find_element(By.XPATH, '/html/body/div[2]/input').get_attribute("value")
        assert cep == ""
    
    def test_NaoAdicionando_EmpresaProx(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[4]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/button[1]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/form/button').click()
        time.sleep(1)
        popup = self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]')
        assert popup is not None

    def test_Basico_Simulador(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[5]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[1]/div/label[3]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[2]/div/label[9]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[3]/input').send_keys('35')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/resultados"
    
    def test_Novamente_simulador(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[5]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[1]/div/label[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[2]/div/label[6]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[3]/input').send_keys('46')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/main/section/div[2]/a[1]').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/simulador"

    def test_Orcamento_simulador(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[1]/div[5]/a/img').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[1]/div/label[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[2]/div/label[6]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/div[3]/input').send_keys('46')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/main/section/form/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/main/section/div[2]/a[2]').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/orcamento"

    def test_Enviar_Feedback(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/i/div[4]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/p[1]/input').send_keys('Nome')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/p[2]/input').send_keys('Sobrenome')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/p[3]/input').send_keys('Cidade') 
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/p[4]/select/option[6]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/p[5]/select/option[5]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/p[1]/input').send_keys('Boa')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/form/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000"
