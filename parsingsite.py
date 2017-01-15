# Прога ищет стримы русскоговорящих программистов на сайте
# https://www.liveedu.tv/




# elem.attrib - получаем атрибуты
# elem.text - текстовые данные
# elem.keys() - список атрибутов
# elem.values() - список значений атрибутов
# etree.tounicode(elem) - сорцы в юникоде
# etree.tostring(elem) - сорцы байтами

def searchRusProgInLiveedu():
    # Функция ищет стримы русскоговорящих программистов на сайте
    # https://www.liveedu.tv/ и возвращает список названий и ссылок

    # elem.attrib - получаем атрибуты
    # elem.text - текстовые данные
    # elem.keys() - список атрибутов
    # elem.values() - список значений атрибутов
    # etree.tounicode(elem) - сорцы в юникоде
    # etree.tostring(elem) - сорцы байтами

    from grab import Grab
    from lxml import etree

    # list = []
    # g = Grab()
    # resp = g.go('https://www.liveedu.tv/livestreams/')

    # for elem in resp.tree.xpath('.//div[@class="browse-main-videos--item"]'):
    #
    #     # Преобразуем елемент в строку а потом в документ HTML
    #     # для дальнейшего парсинга
    #     elem = etree.HTML(etree.tounicode(elem))
    #
    #     flag = elem.xpath('//img[@class="country-flag"]')
    #     title = elem.xpath('//span[@class="browse-main-videos--title"]/a/span')
    #     link = elem.xpath('//a[@class="browse-main-videos--thumbnail  "]')
    #
    #     try:
    #         flag_text = flag[0].attrib['alt']
    #         if flag_text in ['Russia', 'Ukraine', 'Belarus']:
    #             title_text = title[0].text
    #             link_text = link[0].attrib['href']
    #             list.append([title_text, link_text])
    #
    #     except:
    #         pass
    #
    # return list


    # С обьектом select работает метод html() - возвращает сорцы

    g = Grab()
    g.go('https://www.liveedu.tv/livestreams/')
    for elem in g.doc.select('.//div[@class="browse-main-videos--item"]'):
        for flag in elem.select('//img[@class="country-flag"]/@alt'):
            #print(flag.text())
            if flag.text() in ['Russia', 'Ukraine', 'Belarus']:
                for title in elem.select('//span[@class="browse-main-videos--title"]/a/span'):
                    print(title.text())
                #print(flag.text())



        # title = elem.xpath('//span[@class="browse-main-videos--title"]/a/span')
        # link = elem.xpath('//a[@class="browse-main-videos--thumbnail  "]')


if __name__ == '__main__':

    result = open('result.txt', 'wt', encoding='utf-8')
    for i in searchRusProgInLiveedu():
        result.write('Title: ' + i[0] + '\n' + 'Link: https://www.liveedu.tv' + i[1] + '\n\n')
    result.close()
    print('Парсинг завершен.')
    input('Нажмите кнопку чтобы закрыть...')
