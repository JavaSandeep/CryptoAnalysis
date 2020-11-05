import unittest

from adts.structs import AssetNode, LinkedListNode, TradesEdge
from adts.linkedlist import LinkedList
from adts.graph import Graph


class TestLinkedList(unittest.TestCase):

    def test_add_edge(self):
        g=Graph()
        node1=AssetNode(name='TestCase1',symbol='TestCase1')
        node2=AssetNode(name='TestCase2',symbol='TestCase2')
        edge=TradesEdge(
            start=node1,
            end=node2
        )
        self.assertTrue(g.add_edge(edge))

    def test_get_edge_count(self):
        g=Graph()
        node1=AssetNode(name='TestCase1',symbol='TestCase1')
        node2=AssetNode(name='TestCase2',symbol='TestCase2')
        node3=AssetNode(name='TestCase3',symbol='TNT3')
        edge1=TradesEdge(
            start=node1,
            end=node2
        )
        edge2=TradesEdge(
            start=node2,
            end=node3
        )
        edge3=TradesEdge(
            start=node1,
            end=node3
        )

        g.add_edge(edge1)
        self.assertEqual(g.get_edge_count(),1)
        g.add_edge(edge2)
        self.assertEqual(g.get_edge_count(),2)
        g.add_edge(edge3)
        self.assertEqual(g.get_edge_count(),3)

    def test_get_vertex_count(self):
        g=Graph()
        node1=AssetNode(name='TestCase1',symbol='TestCase1')
        node2=AssetNode(name='TestCase2',symbol='TestCase2')
        node3=AssetNode(name='TestCase3',symbol='TNT3')
        edge1=TradesEdge(
            start=node1,
            end=node2
        )
        edge2=TradesEdge(
            start=node2,
            end=node3
        )
        edge3=TradesEdge(
            start=node1,
            end=node3
        )

        g.add_edge(edge1)
        self.assertEqual(g.get_vertex_count(),2)
        g.add_edge(edge2)
        self.assertEqual(g.get_vertex_count(),3)
        g.add_edge(edge3)
        self.assertEqual(g.get_vertex_count(),3)

    def test_getAdjacent(self):
        g=Graph()
        node1=AssetNode(name='TestCase1',symbol='TestCase1')
        node2=AssetNode(name='TestCase2',symbol='TestCase2')
        node3=AssetNode(name='TestCase3',symbol='TNT3')
        node4=AssetNode(name='TestCase3',symbol='TNT3')
        edge1=TradesEdge(
            start=node1,
            end=node2
        )
        edge2=TradesEdge(
            start=node1,
            end=node3
        )
        edge3=TradesEdge(
            start=node2,
            end=node3
        )

        g.add_edge(edge1)
        g.add_edge(edge2)
        g.add_edge(edge3)

        testList=LinkedList()
        testList.insert(node2)
        testList.insert(node3)

        a=g.get_adjacent(node1)
        # print(a)
        self.assertEqual(a.__str__(), testList.__str__())

    def test_dfs(self):
        g=Graph()
        node1=AssetNode(name='TestCase1',symbol='TC1')
        node2=AssetNode(name='TestCase2',symbol='TC2')
        node3=AssetNode(name='TestCase3',symbol='TC3')
        node4=AssetNode(name='TestCase4',symbol='TC4')
        node5=AssetNode(name='TestCase5',symbol='TC5')
        edge1=TradesEdge(
            start=node1,
            end=node2
        )
        edge2=TradesEdge(
            start=node2,
            end=node3
        )
        edge3=TradesEdge(
            start=node2,
            end=node4
        )
        edge5=TradesEdge(
            start=node3,
            end=node5
        )
        edge6=TradesEdge(
            start=node4,
            end=node1
        )
        edge7=TradesEdge(
            start=node1,
            end=node5
        )
        self.assertTrue(g.add_edge(edge1))
        self.assertTrue(g.add_edge(edge2))
        self.assertTrue(g.add_edge(edge3))
        self.assertTrue(g.add_edge(edge5))
        self.assertTrue(g.add_edge(edge6))
        self.assertTrue(g.add_edge(edge7))

        g.dfs(node1, node5, LinkedList(), LinkedList(), LinkedList())
        self.assertEqual(g.list_paths.length, 2)

if __name__=='__main__':
    unittest.main()
