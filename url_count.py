#!/usr/bin/env python
#encoding=utf-8

import sqlite3
from urlparse import urlparse,urljoin

#�ֵ䱣֤��{��name��:1,}��ʽ
#����һ��url���д��?����ֵ���û�У��¼ӣ����У��ֵ�url��count����1
class url_deal(object):
    def __init__(self,url,dict):
        self.url = url
        self.dict = dict
        
    def getDomain(self):
        #��һ��url���н���������http://www.baidu.com/index.php?id=1---->(scheme='http',netloc='www.baidu.com',path='/index.php',params='',query='id=1',fragment='')
        parsedurl = urlparse(self.url,'http:',0)
        domain = parsedurl[0] +'://'+ parsedurl[1]
        return domain
    
    def add(self):
        domain = self.getDomain()
        #�����ֵ�����url
        if self.dict.has_key(domain) == False:
            self.dict.setdefault(domain,1)
            return 
        self.dict[domain] = self.dict[domain] + 1
        return 
#注意，dict传进来不是字典，而是列表，排序之后就变成列表了
def display(dict):
    result = open(r'url.html','w')
    result.write('<html>\n')
    result.write('<title>url result</title>\n')
    result.write('<head>url analyse</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>url</th>\n')
    result.write('<th>count</th>\n')
    result.write('</tr>\n')
    for i in range(len(dict)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(dict[i][0])
        result.write('</td>\n')
        result.write('<td>')
        result.write(str(dict[i][1]))
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

def main(filepath):
    url_dir = {}
    c = 0
    con = sqlite3.connect(filepath)
    cur = con.cursor()
    cur.execute("select url from urls")
    res = cur.fetchone()
    while res:
        for line in res:
            pass
        url = url_deal(line,url_dir)
        url.add()
        c = c + 1
        res = cur.fetchone()
    url_sorted = sorted(url_dir.iteritems(),key = lambda asd:asd[1],reverse = True)
    display(url_sorted)
 
        
    cur.close()
    con.close()

        
        
        
        
    






