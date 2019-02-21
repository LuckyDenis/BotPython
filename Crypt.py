# coding: utf8

import hmac
import hashlib


class MD5Hash:
    def __init__(self):
        self._hash = None
        self._login = None

    def get_hash(self, login: str, passhash, key):
        self._login = login.encode('ascii')
        self._hash = hmac.new(passhash, key, hashlib.md5).hexdigest()
        return self._hash

    def get_key(self, key):
        new_hash = bytearray([i for i in range(len(self._hash) + len(key))])

        for i in range(len(self._hash)):
            new_hash[i] = self._hash[i]

        for i in range(len(key)):
            new_hash[i + len(self._hash)] = key[i]

        return hmac.new(self._login, new_hash, hashlib.md5).hexdigest()


class MPPC:
    def __init__(self):
        self._dec_history = bytearray().append(0xffff)
        self._srcbinary = bytearray()

    def pack(self, src):
        outputbits = bytearray([i for i in range((src.Length * 9) + 11)])
        arr2 = bytearray(src)
        self.re_order_bit_array(arr2)

    def copy(self,  inputbits, outputbits, to, frm, length):
        for i in range(0, length):
            outputbits[to + i] = inputbits[frm + i]

    def re_order_bit_array(self, src):
        for i in range(0, len(src), 8):
            for j in range(0, 4):
                flag = src[i + j]
                src[i + j] = src[i + (j - 7)]
                src[i + (7 - j)] = flag
