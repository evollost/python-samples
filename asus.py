# coding=utf-8  
import requests  
import urllib2
import sys
import cookielib
import re
import smtplib
from email.mime.text import MIMEText
#华硕网申招聘状态查询，邮件发送最新状态

def send_mail(status):
	sender = 'xxx'#发件箱地址  
	receiver = 'xxx' #收件箱地址
	subject = '最新面试状态:'+status  #主题
	smtpserver = 'smtp.xxx'#smtp服务器地址  
	username = 'xxx'  #发件箱地址
	password = 'xxx'  #发件箱密码
	msg = MIMEText('华硕招聘:http://asus.hirede.com/UserCenter/CampusJobApplication/ApplicationDetails', _subtype='html', _charset='utf-8')
	msg['Subject'] = subject   
	smtp = smtplib.SMTP()  
	smtp.connect('smtp.xxx')  
	smtp.login(username, password)  
	smtp.sendmail(sender, receiver, msg.as_string())  
	smtp.close()

s = requests.Session()
type = sys.getfilesystemencoding()
user='xxx'
password='xxx'
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
token = patten.search(res).group(1) #获取登录token值


login_data = {'UserName': user, 'Password': password, 'RememberMe':'false', '__RequestVerificationToken': token}  

#登录
s.post('http://asus.hirede.com/UserCenter/Account/Login', login_data, headers=headers)  
f = s.get('http://asus.hirede.com/UserCenter/CampusJobApplication/ApplicationDetails', headers=headers2).content
pat = re.compile('当前状态：\<span class="text-success"\>\S*\<\/span')
result = pat.search(f).group(0).decode("utf-8")
re_words = re.compile(ur"[\u4e00-\u9fa5]+")  
m =  re_words.findall(result)
status = m[1].encode("utf-8")
if status != '筛选中':
    send_mail(status)
