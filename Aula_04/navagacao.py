"""
BUSCA ANINHADA -> é a busca de algo que está dentro de uma tag

                    HIERARQUIA
    <body>                
        <p> paragrafo
            <ul> lista não ordenada
                <li> item da lista
                    <a> ancora

""" 
#  Importaçãp
from selenium import webdriver  
from time import sleep

#  Acessando o browser e o site
browser = webdriver.Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')
sleep(2)

#  1 -> Acessando a tag "ul"
lista_nao_ordenada = browser.find_element_by_tag_name('ul')

#  2 -> Acessando a tag "li" a partir da tag "ul" já coletada
lis = lista_nao_ordenada.find_elements_by_tag_name('li')
print(f'O tamanho de lis é {len(lis)}')
print(lis[0].text)
print(lis[1].text)

#  3 -> Pegando o texto do elemento através de seu índice
lis0 = lis[0].find_element_by_tag_name('a').text  # vai pegar somente o texto da tag "a" referente ao ind.
print(lis0)

browser.quit()


"""
1 -> buscou a ul
2 -> buscou a li dentro da ul encontrada
3 -> pegou-se o valor de a dentro da li, distinguindo de qual li através do indice

find_element_by_tag_name: pega a primeira tag da hierarquia
find_elements_by_tag_name: pega todas as tag
"""


