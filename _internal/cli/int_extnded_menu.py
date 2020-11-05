class InteractiveExtendedMenu:
    def __call__(self, option_1, option_2=None):
        """
        Function to act as the option to function mapping
        params option 1: First input from user
        params option 2: Second input from user, depends on param 1
        """
        arg1,arg2=None,None
        is_continue=True

        if option_1==1:
            # It has three more hidden option
            if option_2==1:
                # get the file name
                arg1=input("Enter the asset data file name (asset_info.csv): ")
            elif option_2==2:
                arg1=input("Enter the trade data file name (trade_info.json): ")
            elif option_2==3:
                arg1=input("Enter the asset file name to be loaded (asset_list.pickle) :")
                arg2=input("Enter the trade file name to be loaded (graph_trade_info.pickle) :")
        elif option_1==2:
            arg1=input("Enter the asset symbol (eg: BTC): ")
        elif option_1==3:
            arg1=input("Enter the trade symbol (eg: ETHBTC): ")
        elif option_1==4:
            arg1=input("Enter the base asset symbol (eg: BTC): ")
            arg2=input("Enter the quote asset symbol (eg: ETH): ")
        elif option_1==5:
            arg1=input("Enter the asset symbol (eg: BTC): ")
        elif option_1==8:
            arg1=input("Enter the asset file name to be saved as (asset_list.pickle) :")
            arg2=input("Enter the trade file name to be saved as (graph_trade_info.pickle) :")
        elif option_1==9:
            is_continue=False

        # List is used to convert to tuple
        return tuple([arg1, arg2]), is_continue
