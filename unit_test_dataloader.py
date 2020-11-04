import unittest

from _internal.adts.linkedlist import LinkedList
from _internal.adts.graph import Graph
from _internal.data_loader import DataLoader


class TestLinkedList(unittest.TestCase):

    def test_load_trade(self):
        ll=LinkedList()
        g=Graph()

        _dataloader=DataLoader()

        ll,g=_dataloader.load_trade(ll, g)
        print(ll.length)
        print(g)

if __name__=='__main__':
    unittest.main()
