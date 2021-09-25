"""
browser.current_url: retorna a url do momento

Para entender as url:
    import urllib
    urlparse(browser.current_url)

browser.refresh:  atualiza a página
browser.title: mostra o título da página

"""

from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')


url_parseada = urlparse(browser.current_url)

print(url_parseada)

browser.quit()
