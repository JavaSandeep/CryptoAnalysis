import unittest

from structs import AssetNode, LinkedListNode
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_is_linkedlist(self):
        """
        function to test if instance created is LinkedList or not
        """
        self.assertIs(type(LinkedList()), LinkedList)
        self.assertNotIsInstance(type(5), LinkedList)

        # Testing if is linked list
        llist = LinkedList()
        llist.insert_first(
                AssetNode(
                    name='TestCase',
                    symbol='TestCase',
                    price='TestCase',
                    volume='TestCase',
                    market_cap='TestCase'
                )
        )
    
    def test_is_empty(self):
        """
        function to test if instance created is empty or not
        """
        self.assertTrue(LinkedList().is_empty)

        # Testing not empty
        llist = LinkedList()
        llist.insert_first(
            AssetNode(
                name='TestCase',
                symbol='TestCase',
                price='TestCase',
                volume='TestCase',
                market_cap='TestCase')
        )
        self.assertFalse(llist.is_empty)

    def test_find(self):
        ll1=AssetNode(name='TestCase',symbol='TestCase')
        ll2=AssetNode(name='TestCase2',symbol='TestCase2',price='TestCase2',volume='TestCase2',market_cap='TestCase2')
        ll3=AssetNode(name='TestCase3',symbol='TestCase3',price='TestCase3',volume='TestCase3',market_cap='TestCase3')
        ll4=AssetNode(name='TestCase4',symbol='TestCase4',price='TestCase4',volume='TestCase4',market_cap='TestCase4')

        llist = LinkedList()
        llist.insert_first(ll1)
        llist.insert_last(ll2)
        llist.insert_last(ll3)

        self.assertTrue(llist.find(ll1))
        self.assertTrue(llist.find(ll2))
        self.assertTrue(llist.find(ll3))
        self.assertFalse(llist.find(ll4))

    def test_linkedlist_length(self):
        ll1=LinkedListNode(AssetNode(name='TestCase',symbol='TestCase'))
        ll2=LinkedListNode(AssetNode(name='TestCase2',symbol='TestCase2',price='TestCase2',volume='TestCase2',market_cap='TestCase2'))
        ll3=LinkedListNode(AssetNode(name='TestCase3',symbol='TestCase3',price='TestCase3',volume='TestCase3',market_cap='TestCase3'))
        ll4=LinkedListNode(AssetNode(name='TestCase4',symbol='TestCase4',price='TestCase4',volume='TestCase4',market_cap='TestCase4'))

        llist = LinkedList()
        llist.insert_first(ll1)
        self.assertEqual(llist.length, 1)
        llist.insert_last(ll2)
        self.assertEqual(llist.length, 2)
        llist.insert_last(ll3)
        self.assertEqual(llist.length, 3)

    def test_sort(self):
        ll1=AssetNode(name='TestCase',symbol='TestCase',price=50,volume='TestCase1',market_cap='TestCase2')
        ll2=AssetNode(name='TestCase2',symbol='TestCase2',price=20,volume='TestCase2',market_cap='TestCase2')
        ll3=AssetNode(name='TestCase3',symbol='TestCase3',price=70,volume='TestCase3',market_cap='TestCase3')
        ll4=AssetNode(name='TestCase4',symbol='TestCase4',price=40,volume='TestCase4',market_cap='TestCase4')

        llist = LinkedList()
        llist.insert_first(ll1)
        llist.insert_last(ll2)
        llist.insert_last(ll3)
        llist.insert_last(ll4)

        print(llist)
        blistt=llist.sort('price')
        print(blistt)


if __name__=='__main__':
    unittest.main()