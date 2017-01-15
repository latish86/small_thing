from random import random
from grab import *
from lxml import etree


# elem.attrib - получаем атрибуты
# elem.text - текстовые данные
# elem.keys() - список атрибутов
# elem.values() - список значений атрибутов
# etree.tounicode(elem) - сорцы в юникоде
# etree.tostring(elem) - сорцы байтами

def main():
    g = Grab()
    # resp = g.go('https://habrahabr.ru/')
    # result = open('result.txt','at', encoding='utf-8')
    # for elem in Bresp.tree.xpath('.//*[@class="post__header"]/span'):
    #     print(elem.text)
    #     result.write(elem.text.strip()+'\n')

    # resp = g.go('https://nstarikov.ru/blog')
    # result = open('result.txt','wt', encoding='utf-8')
    # for elem in resp.tree.xpath('.//*[@class="feed"]/article/a/figure/strong'):
    #     print(elem)
    #     result.write(elem.text.strip()+'\n')

    resp = g.go('http://top.artlebedev.ru')
    result = open('result.txt','wt', encoding='utf-8')
    for elem in resp.tree.xpath('.//div[@class="post_info"]'):
        print(etree.tounicode(elem))
        try:
            pass
            result.write(etree.tounicode(elem)+'\n')
            # result.write(elem.text.strip()+'\n')
        except:
            pass

    result.close()



if __name__ == '__main__':
    main()
