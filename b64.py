# /usr/bin/python
# encoding: utf-8
from utils import *
_PADCHAR = "="
_ALPHA = "LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA"


def _getbyte64(s,i):
    idx=_ALPHA.find(s[i])
    if idx == -1:
        print("Cannot decode base64")
        exit()
    return idx

def _getbyte(s, i):
    x = ord(s[i])
    if x > 255:
        print("INVALID_CHARACTER_ERR: DOM Exception 5")
        exit()
    return x

def encode_b64(s):
        # if (arguments.length !== 1) {
        #     throw "SyntaxError: exactly one argument required"
        # }
        # s = String(s);
        x = []
        imax = len(s) - len(s) % 3
        if len(s) == 0:
            return s
        i=0
        while i<imax:
            b10 = (_getbyte(s, i) << 16) | (_getbyte(s, i + 1) << 8) | _getbyte(s, i + 2)
            x.append(_ALPHA[b10 >> 18])
            x.append(_ALPHA[(b10 >> 12) & 63])
            x.append(_ALPHA[(b10 >> 6) & 63])
            x.append(_ALPHA[b10 & 63])
            i+=3
        if len(s) - imax==1:
            b10 = _getbyte(s, i) << 16
            x.append(_ALPHA[b10 >> 18] + _ALPHA[(b10 >> 12) & 63] + _PADCHAR + _PADCHAR)
        elif len(s) - imax==2:
            b10 = (_getbyte(s, i) << 16) | (_getbyte(s, i + 1) << 8)
            x.append(_ALPHA[b10 >> 18] + _ALPHA[(b10 >> 12) & 63] + _ALPHA[(b10 >> 6) & 63] + _PADCHAR)
        return "".join(x)

def decode_b64(s):
    pads = 0
    imax = len(s)
    x = []
    # s = String(s);
    if  imax == 0:
        return s
    if imax % 4 != 0:
        print("Cannot decode base64")
        exit()
    if s[imax - 1] == _PADCHAR:
        pads = 1
        if s[imax - 2] == _PADCHAR:
            pads = 2
        imax -= 4
    i=0
    while i<imax:
        b10 = (_getbyte64(s, i) << 18) | (_getbyte64(s, i + 1) << 12) | (_getbyte64(s, i + 2) << 6) | _getbyte64(s, i + 3)
        x.append(fromCharCode(b10 >> 16, (b10 >> 8) & 255, b10 & 255))
        i+=4
    if pads==1:
        b10 = (_getbyte64(s, i) << 18) | (_getbyte64(s, i + 1) << 12) | (_getbyte64(s, i + 2) << 6)
        x.append(fromCharCode(b10 >> 16, (b10 >> 8) & 255))
    elif pads==2:
        b10 = (_getbyte64(s, i) << 18) | (_getbyte64(s, i + 1) << 12)
        x.append(fromCharCode(b10 >> 16))
    return "".join(x)