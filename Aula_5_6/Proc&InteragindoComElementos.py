"""
Procurando e interagindo com elementos

ATRIBUTOS GLOBAIS: são atributos que podem ter em todos os elementos da web

ID é uma atributo global, mas com um valor UNICO.
Ex.: b.find_element_by_id('//valor do id')

TAG: é um atributo global


EXEMPLOS:
b.find_element_by_id('//valor do id')  # resultado mais expecífico
b.find_element_by_tag_name('//nome da tag')  # resultado menos precíso



##                                   ATRIBUTO GLOBAL: CLASS
        Buscam vários elementos que fazem parte da mesma classe
b.find_element_by_class_name('//nome da classe')  # pega a primeira classe que encontrar
b.find_elements_by_class_name('//nome da classe')  # pega todas as classes

OBS.: PODE-SE USAR UM .find DENTRO DE OUTRO .find PARA BUSCAR UM RESULTADO MAIS EXPECÍFICO

EX.: b.find_elements_by_class_name('//nome da classe').find_element_by_id('//valor do id')



    EXEMPLO: Buscando uma classe chamada linguagens:
classe = b.find_elements_by_class_name('linguagens')  # irá retornar uma lista
for c in classe:ggg
    print(c.find_element_by_tag_name(h2).text)  # imprimi o texto contigo dentro da TAG h2

                                    OUTROS ATRIBUTOS GLOBIAS
        Atributo global "autofocus": foca em determinado elementos quando a página abre
        Atributo global "Acess Keys": tecla de atalho para determinados elementos
        Atributo global "title": é a mensagem mostrada quando o curso para em cima de um
    determinado elemento
        Atributo global "hidden": Oculta objetos



                                    ELEMENTOS DA WEB
    ELEMENTO INPUT:
        Qualquer elemento web que o usuário possa interagir colocando ou selecionando dados

        EX.: b.find_element_by_name('//nome do input')

            PARA DIGITAR EM INPUT'S
                EX.: b.find_element_by_name('//nome do input')  # seleciona
                    b.sind_keys('alguma coisa')  # digita       /    send_keys = enviar teclas

            PARA CLICAR EM INPUT'S
                EX.: b.find_element_by_name('//nome do input').click()

    ELEMENTO FORM:
        São elementos que contém(aninham) os elementos responsáveis pelos input's do usuário

        PARÂMETRO TARGET: para onde vai redirecionar a página
        PARÂMETRO METHOD: método de envio - url ou escondido
        PARÂMETRO ACTION: onde será feita a requisição - url atual ou em outra

    OBS.: Para pegar a url de uma página:
        from urllib.parse import urlparse
        url = urlparse(b.current_url)


                                    SELETORES
    SELETORES:
        são maneiras de encontrar elementos dentro de uma estrutura HTML ou XML que tem uma
    sintaxe própria e nomenclatura própria

        CSS SELECTOR:
            BÁSICOS: busca por classes, id, elementos mais comuns
            SELETOR DE  GRUPO: junta dois seletores
            COMBINADORES: combina características de mais de um seletor

                BÁSICOS:
                    ID: representado por # em css {b.find_element_by_css_selector(#valor do id)}
                    TAG: representado somente pelo própria nome da tag
                    CLASSE: representado por . em css {b.find_element_by_css_selector(.nome da class)}

                        EXEMPLOS:
                            Buscando só tag: b.find_element_by_css_selector('div')
                            Buscando tag+class: b.find_element_by_css_selector('div.class')
                            Buscando só id: b.find_element_by_css_selector('#id')
                            Buscando só class: b.find_element_by_css_selector('.class')

                    ATRIBUTO: representado por [] em css
                    ATRIBUTO VIA TIPO: representado por [type] em css
                    ATRIBUTO OPERADOR VALOR: representado por [atributo=valor] em css

                        EXEMPLOS:
                            Somente os que tiverem exatamente esse seletor
                                b.find_element_by_css_selector([class='form_group'])
                            Todos os atributos "class" em que a palavras "group" exista
                                b.find_element_by_css_selector([class*='group'])
                            Todos os atricutos "type" que o final do valor seja "t"
                                b.find_element_by_css_selector([type$="t"])

                    COMBINANDO SELETORES:
                        É possivel combinar seletores para ter buscas mais expecíficas

                        EXEMPLOS:
                            Todas as tag "input" com o atributo "type" que o final do seu valor seja "t"
                                b.find_element_by_css_selector('input[type$="t"])

                SELETORES DE GRUPO:
                    POR LISTA: usa uma lista com os parâmetros

                        EXEMPLOS:
                            Qualquer tag "label" juntamente com qualquer tag "input"
                                b.find_element_by_css_selector("label, input")
                            Qualquer tag "label" que contenha o valor for, juntamente a quaisquer
                        tags(*) que contenham o atributo "type" com o valor que termine em "t"
                                b.find_element_by_css_selector('label[for], *[type$="t"])

                SELETORES COMBINADORES:
                    IRMÃOS ADJACENTES: encontra encontra uma tag, após uma determinada tag, no mesmo nível de hierarquia

                        EXEMPLO:
                            Encontrando todas as "br" após a "div", no mesmo nível hierárquico
                                b.find_element_by_css_selector('div + br')

                    GERAL ADJACENTE: encontra todas as tag que estejam no mesmo nível de determinada tag

                        EXEMPLO:
                            Encontrando todas as tag "div" que estejam no mesmo nível de "h2"
                                b.find_element_by_css_selector('div ~ br')

                    FILHOS: encontra todas as tag filhas de uma outra determinada tag

                        EXEMPLO:
                            Encontrando todas as tag "br" que sejam filhas da tag "div"
                                b.find_element_by_css_selector('div > br')

                    DECENDENTES: encontra todas as tag, que sejam filhas de outra tag, direta ou indiretamente

                        EXEMPLO:
                            Encontrando todas as tag "br" que sejam filhas de "form", direta ou indiretamente
                                b.find_element_by_css_selector('form br')

                SELETOR UNIVERSAL:
                    * = qualquer coisa

                        EXEMPLO:
                            b.find_element_by_css_selector(*)








"""
