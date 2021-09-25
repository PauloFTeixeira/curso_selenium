"""
Pegar todos os links de aulas
Navegar até o exercício 3

"""
from selenium.webdriver import Firefox


browser = Firefox()
browser.get("http://selenium.dunossauro.live/aula_04.html")


def link(browser, elemento):

    dicr_link = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_element_by_tag_name('a')
    for ancora in ancoras:
        dicr_link[ancora.text] = ancora.get_attribute('href')
    return dicr_link

link(browser, 'aside')

print(dicr_link)
