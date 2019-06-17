#!python

from trie import Trie, TrieNode
import unittest

class TrieTest(unittest.TestCase):

    def test_init(self):
        tree = Trie()
        assert tree.size == 0
        assert tree.is_empty() is True
        tree.insert('hello')
        tree.search('hello') == 'hello'
        tree.search('state') == None

    def test_init_with_list(self):
        tree = Trie([('North Dakota'), ('North Carolina')])
        assert tree.height() == 14
        assert tree.size == 20
        assert tree.root.children[hash('N') % 26].word == 'North Dakota'
        assert tree.root.children[hash('N') % 26].children[hash('o') % 26].children[hash('r') % 26].word == 'North Dakota'
        assert tree.is_empty() is False

    def test_search(self):
        tree = Trie([('cat'), ('catholic'), ('catch')])
        assert tree.search('ca') == 'cat'
        tree.insert('cup')
        assert tree.search('cath') == 'catholic'
        assert tree.search('cu') == 'cup'
        tree.insert('catch')
        print(tree.search('catch'))
        assert tree.search('catch') == 'catch'
        tree.insert('catholicism')
        assert tree.search('catholic') == 'catholic'
