# encoding=utf-8
import json, math
import time
import re
from hashlib import sha1
import requests
from b64 import encode_b64
from md5 import md5
from utils import *
requests.packages.urllib3.disable_warnings()


def s(a, b):
    c = len(a)
    v = []
    for i in range(0, c, 4):
        # print(i>>2)
        v.insert(i >> 2, (ord(a[i]) if i < c else 0) | (ord(a[i + 1]) << 8 if i + 1 < c else 0) | (
            ord(a[i + 2]) << 16 if i + 2 < c else 0) | (ord(a[i + 3]) << 24 if i + 3 < c else 0))
    if b:
        v.insert(len(v), c)
    return v


def l(a, b):
    d = len(a)
    c = d - 1 << 2
    if (b):
        m = a[d - 1]
        if m < c - 3 or m > c:
            return False
        c = m
    for i in range(d):
        ch1 = a[i] & 0xff
        ch2 = unsigned_right_shitf(a[i], 8) & 0xff
        ch3 = unsigned_right_shitf(a[i], 16) & 0xff
        ch4 = unsigned_right_shitf(a[i], 24) & 0xff
        a[i] = fromCharCode(a[i] & 0xff, unsigned_right_shitf(a[i], 8) & 0xff, unsigned_right_shitf(a[i], 16) & 0xff,
                            unsigned_right_shitf(a[i], 24) & 0xff)
    t = ''.join(a)[0:c] if b else ''.join(a)
    return t


def encode(str, key):
    if str == '':
        return ''
    v = s(str.replace(' ', ''), True)
    k = s(key, False)
    # if (k.length < 4)
    #     k.length = 4;
    n = len(v) - 1
    z = v[n]
    y = v[0]
    c = -1640531527
    q = math.floor(6 + 52 / (n + 1))
    d = 0

    while 0 < q:
        q -= 1
        d = d + c & -1
        e = unsigned_right_shitf(d, 2) & 3
        p = 0
        while p < n:
            y = v[p + 1]
            m = int_overflow(unsigned_right_shitf(z, 5) ^ y << 2)
            m += int_overflow(unsigned_right_shitf(y, 3) ^ z << 4 ^ (d ^ y))
            m += int_overflow(k[p & 3 ^ e] ^ z)
            z = v[p] = int_overflow(v[p] + m & -1)
            p += 1
        y = v[0]
        m = int_overflow(unsigned_right_shitf(z, 5) ^ y << 2)
        m += int_overflow(unsigned_right_shitf(y, 3) ^ z << 4 ^ (d ^ y))
        m += int_overflow(k[p & 3 ^ e] ^ z)
        z = v[n] = int_overflow(v[n] + m & -1)
    return l(v, False)


def userInfo(info, token):
    info = json.dumps(info)
    en = encode(info, token)
    en = encode_b64(en)
    t2 = '{SRBX1}' + en
    return '{SRBX1}' + str(en)

    # return l(v, false)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    username = '1'
    passwd = '1'
    jq = 'jQuery112408405073902772235_%s' % (round(time.time()))
    check_url = 'https://login.imu.edu.cn/cgi-bin/rad_user_info?callback=%s&_=%s' % (jq, round(time.time()))
    t = requests.get(check_url, verify=False).text
    login_info = json.loads(re.search('\((.*?)\)', t).groups()[0])
    if login_info['error'] =='ok':
        print('已登录，余额%s元'%login_info['user_balance'])
        input()
        exit()
    challenge_url = 'https://login.imu.edu.cn/cgi-bin/get_challenge?callback=%s&username=%s&ip=%s&_=%s' % (
    jq, username, login_info['client_ip'], round(time.time()))
    t = requests.get(challenge_url, verify=False).text
    info = json.loads(re.search('\((.*?)\)', t).groups()[0])
    login_url = 'https://login.imu.edu.cn/cgi-bin/srun_portal'
    minfo = {
        "username": username,
        'password': passwd,
        "ip": login_info['client_ip'],
        "acid": "4",
        "enc_ver": "srun_bx1"
    }
    token = info['challenge']
    hmd5 = md5(passwd, token)
    ba = userInfo(minfo, token)
    str = token + username
    str += token + hmd5
    str += token + '4'
    str += token + login_info['client_ip']
    str += token + '200'
    str += token + '1'
    str += token + ba
    login_params = {
        'callback':jq,
        'action': 'login',
        'username': username,
        'password': '{MD5}' + hmd5,
        'os': 'Windows 10',
        'name': 'Windows',
        'double_stack': 0,
        'chksum': sha1(str.encode('utf-8')).hexdigest(),
        'info': ba,
        'ac_id': 4,
        'ip': login_info['client_ip'],
        'n': 200,
        'type': 1,
        '_': round(time.time())
    }
    r=requests.get(login_url,params=login_params,verify=False).text
    r = json.loads(re.search('\((.*?)\)', r).groups()[0])
    if r['error']=='ok':
        check_url = 'https://login.imu.edu.cn/cgi-bin/rad_user_info?callback=%s&_=%s' % (jq, round(time.time()))
        t = requests.get(check_url, verify=False).text
        login_info = json.loads(re.search('\((.*?)\)', t).groups()[0])
        if login_info['error'] == 'ok':
            print('已登录，余额%s元' % login_info['user_balance'])
    else:
        print(r['error_msg'])
    input()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
