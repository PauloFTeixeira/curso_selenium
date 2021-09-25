"""
Quando se tem varios 'a', para diferencia-los, pode-se usar:

Por atributo: elemento.get_attribute('atributo')
Por texto: elemento.text

                        ESQUEMA HIERARQUICO
                li

                a
                
            href    texto
li: browser.find_element_by_tag_name('li')
a:  browser.find_element_by_tag_name('a')
href: elemento.get_attribute('href')
texto: elemento.text
"""
from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto "text"
        Argumentos:
            browser: instancia do navegador
            texto: conteúdo que deve estar na tag
            tag: tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)  # elements retorna uma lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """
    Encontra o elemento "a" com o link "link"
        Argumentos
            browser: instancia do navegador
            link: link que será procurado em todas as tag's "a"
    """
    elementos = browser.find_elements_by_tag_name("a")
    for elemento in elementos:
        if link in elemento.get_attribute("href"):
            return elemento


#  abrindo o navegador - buncando pelo texto
browser = Firefox()
browser.get("http://selenium.dunossauro.live/aula_04_a.html")
sleep(2)
#  executando a função
#elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
#print(elemento_ddg.text)

#  executando a função - buscando pelo 'atributo' 
elemento_ddg = find_by_href(browser, "ddg")
print(elemento_ddg.text)

#print(elemento_ddg.get_attribute("href"))

browser.quit()
