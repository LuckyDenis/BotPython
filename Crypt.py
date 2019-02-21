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

