# coding:utf-8

"""
Baidu Transelation
"""

import random
import json
from hashlib import md5
import requests


def transelate(text,from_='zh',to_='en'):
    appid = '20160712000025083' 
    secretKey = 'qHmm1FXf_rp8rhR7O6jh' 
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    
    q = text
    from_lang = from_
    to_lang = to_
    salt = random.randint(32768, 65536)
    sign = "{}{}{}{}".format(appid,q,str(salt),secretKey).encode("utf-8")
    m1 = md5()
    m1.update(sign)
    sign = m1.hexdigest()
    data = {
        "appid":appid,
        "q":q,
        "from": from_lang,
        "to":to_lang,
        "salt":salt,
        "sign":sign
    }
    
    try:
        r = requests.post(url=url,data=data)
        content = json.loads(r.content)
        result = content['trans_result']
    except Exception as e:
        try:
            result = [{'src':text,'dst':content['error_msg']}]
        except:
            result = [{'src':text,'dst':str(e)}]
    finally:
        return result

if __name__ == "__main__":
    print(transelate("中国"))