import unittest

from _internal.adts.linkedlist import LinkedList
from _internal.adts.graph import Graph
from _internal.data_loader import DataLoader


class TestLinkedList(unittest.TestCase):

    def test_asset_load(self):
        _dataloader=DataLoader()

        llist=_dataloader.load_asset(LinkedList(), 'asset_info.csv')
        print("Printing head of the asset list")
        print(llist._head)

    def test_dump_serialize(self):
        ll=LinkedList()
        g=Graph()
        _dataloader=DataLoader()

        _dataloader.dump_serialize(ll, g)
    
    def test_load_serialize(self):
        _dataloader=DataLoader()

        ll,g=_dataloader.load_serialize(asset_file_name='asset_list.pickle', trade_file_name='graph_trade_info.pickle')

    def test_load_trade(self):
        ll=LinkedList()
        g=Graph()

        _dataloader=DataLoader()

        ll,g=_dataloader.load_trade(ll, g)
        print(ll.length)
        print(g.vertices.length)

if __name__=='__main__':
    unittest.main()
