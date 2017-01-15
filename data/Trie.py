#!/usr/bin/env python
# -*- coding: utf-8 -*-

CHAR_RANGE = 26

class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.child = [None] * CHAR_RANGE
        self.words = []

TxT = 'data/engwords.txt'
root = TrieNode()

def buildTrieTree(current, strs, idx):
    if idx == len(strs):
        current.isWord = True
        return
    index = ord(strs[idx]) - ord('a')
    if index < 0 or index >= 26:
        print strs
    if current.child[index] == None:
        current.child[index] = TrieNode()
    current.child[index].words.append(strs)
    buildTrieTree(current.child[index], strs, idx + 1)

def parseTxt():
    lines = []
    with open(TxT) as fd:
        lines = fd.readlines()
    for line in lines:
        line = line.strip().lower()
        buildTrieTree(root, line, 0)

def search(current, strs, idx):
    if idx == len(strs):
        return current.words
    index = ord(strs[idx]) - ord('a')
    if current.child[index] == None:
        return None
    return search(current.child[index], strs, idx + 1)

def query(strs):
    return search(root, strs, 0)