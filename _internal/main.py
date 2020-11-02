from cli.cli import cli_main
from cli.interactive_menu import MainInteractiveMenu
from cli.int_extnded_menu import InteractiveExtendedMenu

from .api import APIManager


def main_menu():
    argv=cli_main()
    i,r=argv.i,argv.r
    # if r is None, it is interactive mode
    if i:
        _mim = MainInteractiveMenu()
        _iem = InteractiveExtendedMenu()
        _api = APIManager()
        
        is_continue=True
        while is_continue:
            opt1, opt2 = _mim()
            g_vars, is_continue=_iem(opt1, opt2)

            if is_continue:
                _api(opt1, opt2, g_vars)
    elif r:
        pass


main_menu()