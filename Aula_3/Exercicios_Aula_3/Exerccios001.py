"""
Exercício 01
Crie um programa com selenium que:

  Gere um dicionário, onde a chave é a tag h1

    O valor deve ser um novo dicionário
    cada chave do valor deverá ser o valor de 'atributo'
    cada valor deve ser o texto contido no elemento

url: https://curso-python-selenium.netlify.app/exercicio_01.html

"""
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
link = "https://curso-python-selenium.netlify.app/exercicio_01.html"
browser.get(link)

sleep(3)

h1 = str(browser.find_element_by_tag_name("h1").text)
ps = (browser.find_elements_by_tag_name("p"))
atri = ps.get_attribute('atributo')

resultado = {}

#for p in ps:
  

print(resultado)

#browser.quit()
