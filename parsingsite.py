# Прога ищет стримы русскоговорящих программистов на сайте
# https://www.liveedu.tv/

# elem.attrib - получаем атрибуты
# elem.text - текстовые данные
# elem.keys() - список атрибутов
# elem.values() - список значений атрибутов
# etree.tounicode(elem) - сорцы в юникоде
# etree.tostring(elem) - сорцы байтами

def search_rus_prog_in_liveedu_lxml_lib(country_filter=[]):
    """ Функция ищет стримы русскоговорящих программистов на сайте
    https://www.liveedu.tv/ и возвращает список названий и ссылок
    Используется библиотека lxml """

    import lxml.html
    from urllib.request import (urlopen,  # Для получения страницы
                                Request)  # Для создания запроса
    # Контейнер для хранения стримов
    streams = []
    # Начальная страница сайта
    main_url = 'https://www.liveedu.tv/livestreams'

    # Создаем запрос
    req = Request(main_url, headers={'User-Agent': 'Mozilla/5.0'})

    # Создаем объект парсинга
    page = lxml.html.parse(urlopen(req))

    # получаем список элементов заданного класса
    flag = page.getroot().find_class('browse-main-videos--item')

    for elem in flag:
        country = elem.cssselect('.country-flag')[0].attrib['alt']
        if country_filter != []:
            if country in country_filter:
                title = elem.cssselect('.browse-main-videos--title a span')[0].text
                link = elem.cssselect('.browse-main-videos--title a')[0].attrib['href']
                streams.append({'country': country,
                                'title': title,
                                'link': link})
        else:
            title = elem.cssselect('.browse-main-videos--title a span')[0].text
            link = elem.cssselect('.browse-main-videos--title a')[0].attrib['href']
            streams.append({'country': country,
                            'title': title,
                            'link': link})

    return streams

if __name__ == '__main__':
    country_filter = ['Russian',
                      'Ukraine',
                      'Belarus',
                      'Germany']

    for i in search_rus_prog_in_liveedu_lxml_lib(country_filter):
        print('Country: {}\nTitle; {}\n'.format(i['country'], i['title']))

