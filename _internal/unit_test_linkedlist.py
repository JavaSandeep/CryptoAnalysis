import unittest

from adts.structs import AssetNode, LinkedListNode
from adts.linkedlist import LinkedList


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

        sorted_list = LinkedList()
        sorted_list.insert(ll2)
        sorted_list.insert(ll4)
        sorted_list.insert(ll1)
        sorted_list.insert(ll3)

        inverse_sorted_list=LinkedList()
        inverse_sorted_list.insert(ll3)
        inverse_sorted_list.insert(ll1)
        inverse_sorted_list.insert(ll4)
        inverse_sorted_list.insert(ll2)
        
        self.assertEqual(llist.sort('price').__str__(), sorted_list.__str__())
        self.assertEqual(llist.sort('price', inverse=True).__str__(), inverse_sorted_list.__str__())

    def test_get_index(self):
        ll1=AssetNode(name='TestCase',symbol='TestCase',price=50,volume='TestCase1',market_cap='TestCase2')
        ll2=AssetNode(name='TestCase2',symbol='TestCase2',price=20,volume='TestCase2',market_cap='TestCase2')
        ll3=AssetNode(name='TestCase3',symbol='TestCase3',price=70,volume='TestCase3',market_cap='TestCase3')
        ll4=AssetNode(name='TestCase4',symbol='TestCase4',price=40,volume='TestCase4',market_cap='TestCase4')

        llist = LinkedList()
        llist.insert_first(ll3)
        llist.insert_last(ll1)
        llist.insert_last(ll4)
        llist.insert_last(ll2)

        self.assertEqual(llist.get_index(0), ll3)
        self.assertEqual(llist.get_index(1), ll1)
        self.assertEqual(llist.get_index(3), ll2)

    def test_remove(self):
        ll1=AssetNode(name='TestCase',symbol='TestCase',price=50,volume='TestCase1',market_cap='TestCase2')
        ll2=AssetNode(name='TestCase2',symbol='TestCase2',price=20,volume='TestCase2',market_cap='TestCase2')
        ll3=AssetNode(name='TestCase3',symbol='TestCase3',price=70,volume='TestCase3',market_cap='TestCase3')
        ll4=AssetNode(name='TestCase4',symbol='TestCase4',price=40,volume='TestCase4',market_cap='TestCase4')
        ll5=AssetNode(name='TestCase5',symbol='TestCase5',price=140,volume='TestCase5',market_cap='TestCase5')

        llist = LinkedList()
        llist.insert_first(ll1)
        llist.insert(ll2)
        llist.insert(ll3)
        llist.insert(ll4)
        llist.insert(ll5)

        head_removed = LinkedList()
        head_removed.insert(ll2)
        head_removed.insert(ll3)
        head_removed.insert(ll4)
        head_removed.insert(ll5)

        tail_removed=LinkedList()
        tail_removed.insert(ll2)
        tail_removed.insert(ll3)
        tail_removed.insert(ll4)

        middle_removed=LinkedList()
        middle_removed.insert_first(ll2)
        middle_removed.insert(ll4)
        
        self.assertTrue(llist.remove_head())
        self.assertEqual(llist.__str__(), head_removed.__str__())

        # Trying to remove node that is already removed
        self.assertFalse(llist.remove(ll1))
        
        self.assertTrue(llist.remove_last())
        self.assertEqual(llist.__str__(), tail_removed.__str__())
        self.assertTrue(llist.remove(ll3))
        self.assertEqual(llist.__str__(), middle_removed.__str__())

    def test_index(self):
        ll1=AssetNode(name='TestCase',symbol='TestCase',price=50,volume='TestCase1',market_cap='TestCase2')
        ll2=AssetNode(name='TestCase2',symbol='TestCase2',price=20,volume='TestCase2',market_cap='TestCase2')
        ll3=AssetNode(name='TestCase3',symbol='TestCase3',price=70,volume='TestCase3',market_cap='TestCase3')

        llist = LinkedList()
        llist.insert_first(ll1)
        llist.insert(ll2)

        setted_list = LinkedList()
        setted_list.insert(ll1)
        setted_list.insert(ll3)

        llist.set_index(1, ll3)
        self.assertTrue(llist.set_index(1, ll3))
        self.assertEqual(llist.__str__(), setted_list.__str__())
        self.assertFalse(llist.set_index(5, ll3))


if __name__=='__main__':
    unittest.main()