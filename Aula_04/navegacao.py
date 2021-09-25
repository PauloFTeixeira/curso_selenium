"""
browser.get('link'): entra na página
browser.back(): volta na página anterior
browser.forward(): avança para a página que estava

"""

from selenium.webdriver import Firefox
from time import sleep


def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto `text`.

        Argumentos:
            - browser = Instancia do browser [firefox, chrome, ...]
            - texto = conteúdo que deve estar na tag
            - tag = tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento


browser = Firefox()
browser.get("http://selenium.dunossauro.live/aula_04_b.html")
sleep(2)

nomes = ['um', 'dois', 'tres', 'quatro']

for nome in nomes:
    find_by_text(browser, 'div', nome).click()

for nome in nomes:
    sleep(0.25)
    browser.back()

for nome in nomes:
    sleep(0.25)
    browser.forward()



