#!/usr/bin/env python
#-*-coding:utf-8-*-

import info
import url_count
import os
import platform
import webbrowser

def display_main():
    result = open(r'main.html','w')
    result.write('<html>\n')
    result.write('<title>all results</title>\n')
    result.write('<head>all results</head>\n')
    result.write('<body>\n')
    result.write("<br /><a href='url.html'>url analyse result </a>")
    result.write(" <br /><a href='user_pass.html'>user and pass </a>")
    result.write(" <br /><a href='user.html'>all users  </a>\n")
    result.write(" <br /><a href='mobile.html'>all mobile </a>\n")
    result.write(" <br /><a href='email.html'>all email </a>\n")
    result.write(" <br /><a href='indenti.html'>all indentity  </a>\n")
    result.write("  <br /><a href='birth.html'>birthday</a>\n")
    result.write(" <br /> <a href='other.html'>other information</a>\n")
    result.write("</body></html>")

if  __name__ == '__main__': 
    user = os.popen('echo %username%').read().strip('\n')
    system = platform.system()
    if system == 'Linux':
        print ('sorry,linux is not supported now')
    if system == 'Windows':
        version = platform.platform()
        if version[8] == '7' or version[8] == '8':
            history_filepath = r'C:\Users\\'+user+'\AppData\Local\Google\Chrome\User Data\Default\History'
            webdata_filepath = r'C:\Users\\'+user+'\AppData\Local\Google\Chrome\User Data\Default\Web Data'
            if os.path.exists(history_filepath) == False:
                #这里可以将目录文件传递进去
                path = raw_input('the default path is no valid,please input your computer login username:')
                history_filepath = r'C:\Users\\'+path+'\AppData\Local\Google\Chrome\User Data\Default\History'
                webdata_filepath = r'C:\Users\\'+path+'\AppData\Local\Google\Chrome\User Data\Default\Web Data'
            url_count.main(history_filepath)
            info.main(webdata_filepath)
            display_main()
            webbrowser.open(r'main.html')
        if version[8] == 'X':
            history_filepath = r'C:\Documents and Settings\\'+user+'\Local Settings\Application Data\Google\Chrome\User Data\Default\History'
            webdata_filepath = r'C:\Documents and Settings\\'+user+'\Local Settings\Application Data\Google\Chrome\User Data\Default\Web Data'
            if os.path.exists(history_filepath) == False:
                #这里可以将目录文件传递进去
                path = raw_input('the default path is no valid,please input your computer login username:')
                history_filepath = r'C:\Documents and Settings\\'+path+'\Local Settings\Application Data\Google\Chrome\User Data\Default\History'
                webdata_filepath = r'C:\Documents and Settings\\'+path+'\Local Settings\Application Data\Google\Chrome\User Data\Default\Web Data'
            url_count.main(history_filepath)
            info.main(webdata_filepath)
            display_main()
            webbrowser.open(r'main.html')
        
   
   
    
    
