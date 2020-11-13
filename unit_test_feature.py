import unittest

from _internal.main import main_menu


class TestLinkedList(unittest.TestCase):

    @unittest.skip("Recommended to run from main program")
    def test_handle_menu(self):
        """
        Show different UI template
        """
        main_menu()
    

if __name__=='__main__':
    unittest.main()
