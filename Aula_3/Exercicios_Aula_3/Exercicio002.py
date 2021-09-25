"""
Exercício 02

    Crie um programa com selenium que
        ● Jogue o jogo
        ● Quando você ganhar o script deve parar de ser executado

url: https://curso-python-selenium.netlify.app/exercicio_02.html

"""


from selenium import webdriver
from time import sleep
browser = webdriver.Firefox()
link = ("https://curso-python-selenium.netlify.app/exercicio_02.html")
browser.get(link)
sleep(3)

p = browser.find_elements_by_tag_name("p")

while (p[-1].text) != "você está fazendo algo errado":
    p = browser.find_elements_by_tag_name("p")
    browser.find_element_by_tag_name("a").click()
sleep(5)

browser.quit()


#  FUNCIONANDO
#  find_elements_by_tag_name encontra um elemente pelo nome da "tag"
#  Pode-se passar como parâmentro o .click(clicar) e o .text(pegar o texto) 