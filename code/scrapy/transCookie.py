# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "gr_user_id=f335e6c7-3166-4251-a11b-6ed56b644045; ll="118209"; __yadk_uid=kNCLfmn123nCEyADXgAqPI3qe9MdVIaM; bid=jUCnOL0I684; ue="liubaiyuan163@163.com"; viewed="1020067_1056461_2143763_10826042_26665636_27041297_3533087_4243207_1941558_25895404"; _ga=GA1.2.166885613.1468324950; _gid=GA1.2.1756975197.1511925594; dbcl2="74518315:U7PQmx1VyXI"; ck=9yjq; ap=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1511931792%2C%22https%3A%2F%2Fwww.google.co.jp%2F%22%5D; _pk_id.100001.8cb4=356401b8bbc256db.1468325216.198.1511932485.1511927405.; _pk_ses.100001.8cb4=*; __utmt=1; __utma=30149280.166885613.1468324950.1511925587.1511929784.401; __utmb=30149280.8.10.1511929784; __utmc=30149280; __utmz=30149280.1511477375.397.237.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=30149280.7451; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=D028DFDDC31E68731AD89343AF5EA032|cbd760369a69bfda6c0392c134d5155f"
    trans = transCookie(cookie)
    print trans.stringToDict()
