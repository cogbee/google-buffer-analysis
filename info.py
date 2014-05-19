#!/usr/bin/env python
#-*-coding:utf-8-*-

import sqlite3
import re
import sys

reload(sys)
sys.setdefaultencoding('gbk')

class rules(object):
    def __init__(self,oneline):
        self.oneline = oneline
        #email,identi在value 中查找，中文我无能为力了暂时 from name
        self.username = re.compile(r'[a-zA-Z_[\]\']*(user|USER|User|Name|NAME|name|account|ACCOUNT|Account|Id|ID|id)[a-zA-Z_[\]\']*')
        self.password = re.compile(r'[a-zA-Z_[\]\']*(pass|Pass|PASS|passwd|Passwd|PASSWD|password|PASSWORD|Password|pwd|Pwd|PWD)[a-zA-Z_[\]\']*')
        self.birthday = re.compile(r'[a-zA-Z_[\]\']*(birth|birthday)[a-zA-Z_[\]\']*')
        self.addr = re.compile(r'[a-zA-Z_[\]\']*(addr|Addr|address|Address)[a-zA-Z_[\]\']*')
        #ctl00系列以及info[]系列
        self.other = re.compile(r'[a-zA-Z_[\]0-9\']*[[a-zA-Z_[\]0-9\']*]$|ctl00$[a-zA-Z_0-9\']*$')
        # from value
        self.email = re.compile(r'[a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.com')
        self.identi = re.compile(r'(\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$')
        self.md5 = re.compile(r'[0-9a-f]{16}|/^[0-9a-f]{32}$')
        self.mobile = re.compile(r'/^1[0-9]{10}$')
        self.stat = []
        
    def getType(self):
        print self.oneline[1]
        match = self.username.match(self.oneline[1])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.password.match(self.oneline[1])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.birthday.match(self.oneline[1])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.addr.match(self.oneline[1])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.other.match(self.oneline[1])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.email.match(self.oneline[2])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.identi.match(self.oneline[2])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.md5.match(self.oneline[2])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        match = self.mobile.match(self.oneline[2])
        if match:
            self.stat.append(1)
        else:
            self.stat.append(0)
        
        return self.stat
def display_user_pass(user_pass):
    result = open(r'user_pass.html','w')
    result.write('<html>\n')
    result.write('<title>user_pass result</title>\n')
    result.write('<head>some user and password</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>username</th>\n')
    result.write('<th>password</th>\n')
    result.write('</tr>\n')
    for i in range(len(user_pass)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(user_pass[i][0])
        result.write('</td>\n')
        result.write('<td>')
        result.write(user_pass[i][1])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

def display_user(user):
    result = open(r'user.html','w')
    result.write('<html>\n')
    result.write('<title>user result</title>\n')
    result.write('<head>some user</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>username</th>\n')
    result.write('</tr>\n')
    for i in range(len(user)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(user[i])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()
    
def display_email(email):
    result = open(r'email.html','w')
    result.write('<html>\n')
    result.write('<title>email result</title>\n')
    result.write('<head>email</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>email</th>\n')
    result.write('</tr>\n')
    for i in range(len(email)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(email[i])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

def display_mobile(mobile):
    result = open(r'mobile.html','w')
    result.write('<html>\n')
    result.write('<title>mobile result</title>\n')
    result.write('<head>mobile</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>mobile</th>\n')
    result.write('</tr>\n')
    for i in range(len(mobile)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(mobile[i])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

def display_birth(birth):
    result = open(r'birth.html','w')
    result.write('<html>\n')
    result.write('<title>birth result</title>\n')
    result.write('<head>birth</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>birth</th>\n')
    result.write('</tr>\n')
    for i in range(len(birth)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(birth[i])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

def display_indenti(indenti):
    result = open(r'indenti.html','w')
    result.write('<html>\n')
    result.write('<title>indenti result</title>\n')
    result.write('<head>id</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>indenti</th>\n')
    result.write('</tr>\n')
    for i in range(len(indenti)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(indenti[i])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()
    
def display_addr(addr):
    result = open(r'addr.html','w')
    result.write('<html>\n')
    result.write('<title>addr result</title>\n')
    result.write('<head>addr</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>addr</th>\n')
    result.write('</tr>\n')
    for i in range(len(addr)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(addr[i])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

def display_other(other):
    result = open(r'other.html','w')
    result.write('<html>\n')
    result.write('<title>other result</title>\n')
    result.write('<head>other</head>\n')
    result.write('<body>\n')
    result.write('<table> \n <tr>\n ')
    result.write('<th>other[0]</th>\n')
    result.write('<th>other[1]</th>\n')
    result.write('</tr>\n')
    for i in range(len(other)):
        result.write('<tr>\n')
        result.write('<td>')
        result.write(other[i][0])
        result.write('</td>\n')
        result.write('<td>')
        result.write(other[i][1])
        result.write('</td>\n')
        result.write('</tr>\n')
    result.write('</table>\n</body>\n</html>\n')
    result.close()

 
def main(filepath):
    user_pass = []
    user = []
    email = []
    mobile = []
    birth = []
    indenti = []
    addr = []
    other = []
    c = 0
    #flag 用来判断user和pass是否在一起
    flag = 0
    con = sqlite3.connect(filepath)
    cur = con.cursor()
    cur.execute("select pair_id,name,value from autofill")
    res = cur.fetchall()
    for i in range(len(res)):
        c = c + 1
        rule = rules(res[i])
        stat = rule.getType()
        if stat[0] == 1:
            user.append(res[i][2])
            if flag == 0:
                flag = 1
            else:
                flag = 0              
        if stat[1] == 1 or stat[7] == 1:
            if flag == 1:
                temp = (res[i-1][2],res[i][2])
                user_pass.append(temp)
            else:
                temp = ('unknow',res[i][2])
                user_pass.append(temp)
            flag = 0
        if stat[2] == 1:
            birth.append(res[i][2])
            flag = 0
        if stat[3] == 1:
            addr.append(res[i][2])
            flag = 0
        if stat[4] == 1:
            other.append((res[i][1],res[i][2]))
            flag = 0
        if stat[5] == 1:
            email.append(res[i][2])
            print 'res:'+res[i][2]
            flag = 0
        if stat[6] == 1:
            indenti.append(res[i][2])
            flag = 0
        if stat[8] == 1:
            mobile.append(res[i][2])
            flag = 0
    
    
    display_other(other)
    display_user_pass(user_pass)
    display_user(user)
    display_email(email)
    display_mobile(mobile)
    display_addr(addr)
    display_birth(birth)
    display_indenti(indenti)
      
    cur.close()
    con.close()
