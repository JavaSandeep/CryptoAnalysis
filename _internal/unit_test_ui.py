import unittest

from cli.interactive_menu import MainInteractiveMenu


class TestLinkedList(unittest.TestCase):

    def test_show(self):
        """
        Show different UI template
        """
        _mim=MainInteractiveMenu()
        _mim.show(_mim.template_main_menu)
        _mim.show(_mim.template_load_data_sub_menu)
        _mim.show(_mim.template_asset_filter_menu)
    
    def test_handle_menu(self):
        """
        Show different UI template
        """
        _mim=MainInteractiveMenu()
        _mim.menu_handle()
    
    def test_is_valid(self):
        """
        Tests is valid method of interactive menu
        valid condition:
            - has to be integer
            - has to between min and max value
        """
        _mim=MainInteractiveMenu()

        self.assertFalse(_mim.is_valid(value=1, min_value=3, max_value=5))
        self.assertTrue(_mim.is_valid(value=2, min_value=1, max_value=5))
        self.assertFalse(_mim.is_valid(value=1.5, min_value=1, max_value=5))

if __name__=='__main__':
    unittest.main()
