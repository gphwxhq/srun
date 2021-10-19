from utils import *


def t(n, t):
    r = int_overflow((65535 & n) + (65535 & t))
    return int_overflow((n >> 16) + (t >> 16) + (r >> 16) << 16 | 65535 & r)

def r(n, t):
    # return n << t | n >>> 32 - t
    return int_overflow(n << t | unsigned_right_shitf(n, 32 - t))

def e(n, e, o, u, c, f):
    return int_overflow(t(r(t(t(e, n), t(u, f)), c), o))

def f(n, t, r, o, u, c, f):
    return int_overflow(e(r ^ (t | ~o), n, t, u, c, f))

def o(n, t, r, o, u, c, f):
    return int_overflow(e(t & r | ~t & o, n, t, u, c, f))

def u(n, t, r, o, u, c, f):
    return int_overflow(e(t & o | r & ~o, n, t, u, c, f))

def c(n, t, r, o, u, c, f) :
    return int_overflow(e(t ^ r ^ o, n, t, u, c, f))

def i(n, r):
    try:
        n[r >> 5] |= 128 << r % 32
    except:
        index=r >> 5
        for i in range(len(n),index+1):
            if i!=index:
                n.append(0)
            else:
                n.append(0| 128 << r % 32)
    try:
        n[14 + (unsigned_right_shitf(r +64, 9) << 4)] = r
    except:
        index=14 + (unsigned_right_shitf(r +64, 9) << 4)
        for i in range(len(n),index+1):
            if i!=index:
                n.append(0)
            else:
                n.append(r)
    l = 1732584193
    g = -271733879
    v = -1732584194
    m = 271733878
    for e in range(0,len(n),16):
        i = l
        a = g
        d = v
        h = m
        # print(l, g, v, m, n[e])
        l = int_overflow(o(l, g, v, m, n[e], 7, -680876936))
        m = int_overflow(o(m, l, g, v, n[e + 1], 12, -389564586))
        v = int_overflow(o(v, m, l, g, n[e + 2], 17, 606105819))
        g = int_overflow(o(g, v , m, l, n[e + 3], 22, -1044525330))
        l = o(l, g, v, m, n[e + 4], 7, -176418897)
        m = o(m, l, g, v, n[e + 5], 12, 1200080426)
        v = o(v, m, l, g, n[e + 6], 17, -1473231341)
        g = o(g, v, m, l, n[e + 7], 22, -45705983)
        l = o(l, g, v, m, n[e + 8], 7, 1770035416)
        m = o(m, l, g, v, n[e + 9], 12, -1958414417)
        v = o(v, m, l, g, n[e + 10], 17, -42063)
        g = o(g, v, m, l, n[e + 11], 22, -1990404162)
        l = o(l, g, v, m, n[e + 12], 7, 1804603682)
        m = o(m, l, g, v, n[e + 13], 12, -40341101)
        v = o(v, m, l, g, n[e + 14], 17, -1502002290)
        if e+15>30:
            g = o(g, v, m, l, 0, 22, 1236535329)
        else:
            g = o(g, v, m, l, n[e + 15], 22, 1236535329)
        l = u(l, g, v, m, n[e + 1], 5, -165796510)
        m = u(m, l, g, v, n[e + 6], 9, -1069501632)
        v = u(v, m, l, g, n[e + 11], 14, 643717713)
        g = u(g, v, m, l, n[e], 20, -373897302)
        l = u(l, g, v, m, n[e + 5], 5, -701558691)
        m = u(m, l, g, v, n[e + 10], 9, 38016083)
        if e + 15 > 30:
            v = u(v, m, l, g, 0, 14, -660478335)
        else:
            v = u(v, m, l, g, n[e + 15], 14, -660478335)
        g = u(g, v, m, l, n[e + 4], 20, -405537848)
        l = u(l, g, v, m, n[e + 9], 5, 568446438)
        m = u(m, l, g, v, n[e + 14], 9, -1019803690)
        v = u(v, m, l, g, n[e + 3], 14, -187363961)
        g = u(g, v, m, l, n[e + 8], 20, 1163531501)
        l = u(l, g, v, m, n[e + 13], 5, -1444681467)
        m = u(m, l, g, v, n[e + 2], 9, -51403784)
        v = u(v, m, l, g, n[e + 7], 14, 1735328473)
        g = u(g, v, m, l, n[e + 12], 20, -1926607734)
        l = c(l, g, v, m, n[e + 5], 4, -378558)
        m = c(m, l, g, v, n[e + 8], 11, -2022574463)
        v = c(v, m, l, g, n[e + 11], 16, 1839030562)
        g = c(g, v, m, l, n[e + 14], 23, -35309556)
        l = c(l, g, v, m, n[e + 1], 4, -1530992060)
        m = c(m, l, g, v, n[e + 4], 11, 1272893353)
        v = c(v, m, l, g, n[e + 7], 16, -155497632)
        g = c(g, v, m, l, n[e + 10], 23, -1094730640)
        l = c(l, g, v, m, n[e + 13], 4, 681279174)
        m = c(m, l, g, v, n[e], 11, -358537222)
        v = c(v, m, l, g, n[e + 3], 16, -722521979)
        g = c(g, v, m, l, n[e + 6], 23, 76029189)
        l = c(l, g, v, m, n[e + 9], 4, -640364487)
        m = c(m, l, g, v, n[e + 12], 11, -421815835)
        if e + 15 > 30:
            v = c(v, m, l, g, 0, 16, 530742520)
        else:
            v = c(v, m, l, g, n[e + 15], 16, 530742520)
        g = c(g, v, m, l, n[e + 2], 23, -995338651)
        l = f(l, g, v, m, n[e], 6, -198630844)
        m = f(m, l, g, v, n[e + 7], 10, 1126891415)
        v = f(v, m, l, g, n[e + 14], 15, -1416354905)
        g = f(g, v, m, l, n[e + 5], 21, -57434055)
        l = f(l, g, v, m, n[e + 12], 6, 1700485571)
        m = f(m, l, g, v, n[e + 3], 10, -1894986606)
        v = f(v, m, l, g, n[e + 10], 15, -1051523)
        g = f(g, v, m, l, n[e + 1], 21, -2054922799)
        l = f(l, g, v, m, n[e + 8], 6, 1873313359)
        if e + 15 > 30:
            m = f(m, l, g, v, 0, 10, -30611744)
        else:
            m = f(m, l, g, v, n[e + 15], 10, -30611744)
        v = f(v, m, l, g, n[e + 6], 15, -1560198380)
        g = f(g, v, m, l, n[e + 13], 21, 1309151649)
        l = f(l, g, v, m, n[e + 4], 6, -145523070)
        m = f(m, l, g, v, n[e + 11], 10, -1120210379)
        v = f(v, m, l, g, n[e + 2], 15, 718787259)
        g = f(g, v, m, l, n[e + 9], 21, -343485551)

        l = t(l, i)
        g = t(g, a)
        v = t(v, d)
        m = t(m, h)
    return [l, g, v, m]

def d(n):
    r = []
    for t in range((len(n) >> 2)):
        r.append(0)
    e = 8 * len(n)
    for t in range(0,e,8):
        try:
            r[t >> 5] |= (255 & ord(n[int(t / 8)])) << t % 32
        except:
            index = t >> 5
            for i in range(len(r), index + 1):
                if i != index:
                    r.append(0)
                else:
                    r.append(0|(255 & ord(n[int(t / 8)])) << t % 32)
    return r

def a(n):
        r = ""
        e = 32 * len(n)
        for t in range(0,e,8):
            r += chr(unsigned_right_shitf(n[t >> 5], t % 32) & 255)
        return r

def l(n, t):
    o = d(n)
    u = []
    c = []
    for it in range(16):
        u.append(0)
        c.append(0)
    if len(o) > 16:
        o = i(o, 8 * len(n))
    for r in range(16):
        u[r] = 909522486 ^ o[r]
        c[r] = 1549556828 ^ o[r]
    e = i(u+d(t), 512 + 8 * len(t))
    return a(i(c+e, 640))

def g(n):
    e = ""
    for r in range(len(n)):
        t = ord(n[r])
        e += "0123456789abcdef"[unsigned_right_shitf(t,4) & 15] + "0123456789abcdef"[15 & t]
    return e

def md5(password,token):
    t=l(token,password)
    return g(t)