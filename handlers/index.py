#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from data import Trie

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        searchKey = self.get_argument("searchKey")
        keyWords = Trie.query(searchKey)
        if keyWords == None:
            keyWords = ""
        else:
            keyWords = ';'.join(list(keyWords))
        self.write(keyWords)

handlers = [
(r"/", IndexHandler),
]