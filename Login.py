# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:01 2017

@author: roger
"""
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()

try:
    (state,reason) = client.login('blue_beer@163.com', 'qi142857')
    print (state,reason)

except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('email_or_phone', 'password', captcha)

client.save_token('./token.pkl')


