import sys
import traceback
import argparse

from .cli_exceptions import NoCLIArgsPassedException

# This module helps as the base CLI for the program
# Do not reimport the module
#@author: Sandeep Dudhraj

def cli_main():
    try:
        parser = argparse.ArgumentParser(prog='cryptoAnalysis',description="Commandline User Interface for the crypto analysis program.")

        parser.add_argument(
            '-r',
            nargs=2,
            action='store',
            metavar=('<asset_file>','<trade_file>'),
            help='Report mode for the cryptoAnalysis program'
        )
        parser.add_argument(
            '-i',
            action='store_true',
            help='Interactive mode for the cryptoAnalysis program'
        )

        args = parser.parse_args()
        
        if (not args.i) and (args.r is None):
            # No arguments passed
            parser.print_help()
            raise NoCLIArgsPassedException

        # Complex data type
        # Namespace
        return args
    except NoCLIArgsPassedException:
        print("Warning. No arguments passed")
        sys.exit(1)
    except Exception as ex:
        print("Error: {0}".format(ex))
        traceback.print_exc()
        sys.exit(1)
