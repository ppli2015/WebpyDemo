# -*-coding:utf-8-*-
__author__ = 'lpp'

import web
import json
import urllib

##urls (argument) - class - page
urls = (
    '/(\index)', 'index',
    '/(\d+)', 'iii',
    '/(\iii)', 'iii',
    '/(\echart)', 'echart',
)
render = web.template.render("templates")


class index:
    def GET(self, name):
        print 'index.GET:', name, '=' * 10
        # argu = [name, 'help']
        # argus = {'a1': '111', 'a2': '222'}
        # return render.test('hh', *argu, **argus)
        return render.index(name)

    def POST(self, name):
        i = web.data()
        query = urllib.unquote(i.split('=')[1])
        print 'index.POST:', name, '=' * 10
        # i = web.input(id=[])
        # ids = i.get('id')
        # print ids

        if query.isdigit() and len(query) == 6:
            raise web.seeother('/' + query)
        else:
            return 'query is : ' + query


class iii:
    def GET(self, name):
        print 'iii.GET:', name, '=' * 10
        code = name
        path = 'C:/Users/Xiang/PycharmProjects/scrapy_stock/tutorial/data_105/'
        try:
            f = open(path + code, 'r')
        except BaseException:
            # print 'file not exist!!!'
            return code + ' is not a stock code!!!'
        else:
            lines = f.readlines()
            str = ''
            for line in lines[:10000]:
                str += line
            res = str.split('☆公司概况☆')[1].split('☆财务分析☆')[0]

            f.close()

            stock_name = res.split('◇')[1].split()[1]
            name_list = res.split('\n')[1].split('】')[:-1]
            for n in range(len(name_list)):
                name_list[n] = name_list[n].split('.')[1]
            res = '\n'.join(res.split('\n')[2:]).strip()
            res_list = res.split('】')[1:]
            for n in range(len(res_list)):
                if res_list[n].find('【'):
                    res_list[n] = res_list[n].split('【')[0]

            # print name_list
            # print len(res_list)
            # print res.decode('utf-8')
            return render.fenlan2(name, stock_name, name_list, res_list)
            # return render.fenlan(name)

    def POST(self, name):
        i = web.data()
        query = i.split('=')[1]
        print 'iii.POST:', name, '=' * 10
        # i = web.input(id=[])
        # ids = i.get('id')
        # print ids

        if query.isdigit() and len(query) == 6:
            raise web.seeother('/' + query)
        else:
            return 'query is : ' + query


class echart:
    def GET(self, name):
        print 'echart.GET:', name, '=' * 10
        f = open('C:/Users/Xiang/PycharmProjects/scrapy_stock/tutorial/data_105/000015', 'r')
        lines = f.readlines()
        str = ''
        for line in lines[:10000]:
            str += line
        res = str.split('☆公司概况☆')[1].split('☆财务分析☆')[0]

        f.close()

        stock_name = res.split('◇')[1].split()[1]
        name_list = res.split('\n')[1].split('】')[:-1]
        for n in range(len(name_list)):
            name_list[n] = name_list[n].split('.')[1]
        res = '\n'.join(res.split('\n')[2:]).strip()
        res_list = res.split('】')[1:]
        for n in range(len(res_list)):
            if res_list[n].find('【'):
                res_list[n] = res_list[n].split('【')[0]

        return render.echart(name, stock_name, name_list, res_list)

    def POST(self, name):
        #
        # i = web.data()
        # year = i.split('=')[1].split('&')[0]
        # keyword = i.split('=')[2]
        # print name,year,keyword
        # # raise web.seeother('/bob')
        # ### get data
        # return '123'

        i = web.data()
        print 'echart.POST:', name, '=' * 10
        print 'web.data: ', i
        file_object = open("1.json","r")
        lines = file_object.readlines()
        data1 = json.dumps(json.loads(lines[0]))
        file_object.close()
        # 获取数据

        return data1


if __name__ == "__main__":
    app = web.application(urls, globals())
    while True:
        try:
            app.run()
        except BaseException:
            pass
