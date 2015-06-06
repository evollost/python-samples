#-*-coding:utf-8-*- 
import requests  
import urllib2
import sys
import cookielib
import re
import smtplib
from email.mime.text import MIMEText

#Monitor Recruitment Status Automatically, you can run it with crontab

def send_mail(status):
    sender = 'xxx'
    receiver = 'xxx'
    subject = ' The latest status:'+status  
    smtpserver = 'smtp.xxx'#smtp address  
    username = 'xxx'  
    password = 'xxx'  
    msg = MIMEText('Recruitment Status:http://asus.hirede.com/UserCenter/CampusJobApplication/ApplicationDetails', _subtype='html', _charset='utf-8')
    msg['Subject'] = subject   
    smtp = smtplib.SMTP()  #required by some smtpserver, such as outlook
    smtp.connect('smtp.xxx')  
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver, msg.as_string())  
    smtp.close()

def Check_Asus(user, password):
    s = requests.Session()
    type = sys.getfilesystemencoding()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',   
        'Referer': 'http://asus.hirede.com/UserCenter/Account/Login',  
        'Host': 'asus.hirede.com'
    }
    headers2 = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }  
    res = s.get('http://asus.hirede.com/UserCenter/Account/Login', headers=headers).content
    patten = re.compile('name="__RequestVerificationToken" type="hidden" value="(\S*)"')   
    #you need random token from the website content
    token = patten.search(res).group(1) 
    login_data = {'UserName': user, 'Password': password, 
        'RememberMe':'false', '__RequestVerificationToken': token}  
    s.post('http://asus.hirede.com/UserCenter/Account/Login', login_data, headers=headers)
    #fetch the latest information
    f = s.get('http://asus.hirede.com/UserCenter/CampusJobApplication/ApplicationDetails', 
        headers=headers2).content
    pat = re.compile('当前状态：\<span class="text-success"\>\S*\<\/span')
    result = pat.search(f).group(0).decode("utf-8")
    re_words = re.compile(ur"[\u4e00-\u9fa5]+")  
    m =  re_words.findall(result)
    status = m[1].encode("utf-8")
    if status != '筛选中':
        send_mail(status)
    
if __name__ == '__main__':
    user = 'xxx'
    password = 'xxx'
    Check_Asus(user, password)