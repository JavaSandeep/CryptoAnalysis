from .adts.linkedlist import LinkedList
from .adts.graph import Graph
from .data_loader import DataLoader

class APIManager:
    def __init__(self):
        self._dloader=DataLoader()
        self.trade=None
        self.assets=None

    def process(self, option_1, option_2, args):
        """
        Function to act as the option to function mapping
        params option 1: First input from user
        params option 2: Second input from user, depends on param 1
        """
        if option_1==1:
            # It has three more hidden option
            if option_2==1:
                # get the file name
                f_name,*_=args
                if f_name=='' or (f_name is None):
                    self.assets=self._dloader.load_asset(LinkedList())
                else:
                    self.assets=self._dloader.load_asset(LinkedList(), f_name)
                print("Number of assets loaded: {0}".format(self.assets.length))
            elif option_2==2:
                # get the file name
                f_name,*_=args
                if not self.assets:
                    print("Asset has not been loaded. Loading assets first..")
                    self.assets=self._dloader.load_asset(LinkedList())
                if f_name=='' or (f_name is None):
                    _,self.trade=self._dloader.load_trade(self.assets, g=Graph())
                else:
                    _,self.trade=self._dloader.load_trade(self.assets, g=Graph(), file_name=f_name)
                print("Number of trades loaded: {0}".format(self.trade.edges.length))
            elif option_2==3:
                asset_file_name, trade_file_name=args
                if asset_file_name=='' or (asset_file_name is None):
                    asset_file_name='asset_list.pickle'
                if trade_file_name=='' or (trade_file_name is None):
                    trade_file_name='graph_trade_info.pickle'
                self.assets, self.trade=self._dloader.load_serialize(asset_file_name, trade_file_name)
                print("Number of assets loaded: {0}".format(self.assets.length))
                print("Number of trades loaded: {0}".format(self.trade.edges.length))
        elif option_1==2:
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            f_name,*_=args
            asset=self.trade.vertices.get_item(f_name)
            if not asset:
                print("No asset found for: {0}".format(f_name))
                return
            print(asset)
        elif option_1==3:
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            f_name,*_=args
            trade=self.trade.edges.get_item(f_name)
            if not trade:
                print("No trade found for: {0}".format(f_name))
                return
            print(trade)
        elif option_1==4:
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            source, dest=args
            if not self.trade.vertices.get_item(source):
                print("Source not in the graph")
                return
            if not self.trade.vertices.get_item(dest):
                print("Destination not in the graph")
                return
            # Reset list paths
            self.trade.reset_list_path()
            # Reset list paths end
            self.trade.dfs(
                self.trade.vertices.get_item(source),
                self.trade.vertices.get_item(dest),
                LinkedList(),
                LinkedList()
            )
            print("Number of paths found: {0}".format(self.trade.list_paths.length))
            print(self.trade.print_paths())
        elif option_1==5:
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            print("Unfortunately. This feature has not been included...")
        elif option_1==6:
            # Description of assets
            # List top 10 assets based on price, volume, market
            # List bottom 10 assets based on price
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            sorted=self.trade.vertices.sort(key='price', inverse=True)
            print("Top 10 assets based on their price")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.name + ' ('+temp.get_symbol+') '+': '+str(temp.price))
            print('\n\n')
            sorted=self.trade.vertices.sort(key='price')
            print("Lowest 10 assets based on their price")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.name + ' ('+temp.get_symbol+') '+': '+str(temp.price))
            print('\n\n')
            sorted=self.trade.vertices.sort(key='volume', inverse=True)
            print("Top 10 assets based on their volume")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.name + ' ('+temp.get_symbol+') '+': '+str(temp.volume))
            print('\n\n')
            sorted=self.trade.vertices.sort(key='market_cap', inverse=True)
            print("Top 10 assets based on their market cap")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.name + ' ('+temp.get_symbol+') '+': '+str(temp.market_cap))
            print('\n\n')
        elif option_1==7:
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            # Description of trade
            print("Statistics on trades based on different properties")
            sorted=self.trade.edges.sort(key='lastPrice', inverse=True)
            print("Top 10 trades based on their last price")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.start_node.get_symbol+' -> '+temp.end_node.get_symbol + ' ('+temp.get_symbol+') '+': '+str(temp.lastPrice))
                # print(sorted.get_index(i))
            print('\n\n')
            sorted=self.trade.edges.sort(key='lastPrice')
            print("Lowest 10 trades based on their last price")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.start_node.get_symbol+' -> '+temp.end_node.get_symbol + ' ('+temp.get_symbol+') '+': '+str(temp.lastPrice))
            print('\n\n')
            sorted=self.trade.edges.sort(key='volume', inverse=True)
            print("Top 10 trades based on their volume")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.start_node.get_symbol+' -> '+temp.end_node.get_symbol + ' ('+temp.get_symbol+') '+': '+str(temp.volume))
            print('\n\n')

            sorted=self.trade.edges.sort(key='count', inverse=True)
            print("Top 10 trades based on their count")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.start_node.get_symbol+' -> '+temp.end_node.get_symbol + ' ('+temp.get_symbol+') '+': '+str(temp.count))
            print('\n\n')
            sorted=self.trade.edges.sort(key='count')
            print("Lowest 10 trades based on their count")
            for i in range(10):
                temp=sorted.get_index(i)
                print(temp.start_node.get_symbol+' -> '+temp.end_node.get_symbol + ' ('+temp.get_symbol+') '+': '+str(temp.count))
            print('\n\n')
        elif option_1==8:
            if not self.trade:
                print("Trade has not been loaded yet..")
                return
            asset_file,trade_file=args
            if asset_file=='' or (asset_file is None):
                asset_file='asset_list.pickle'
            if trade_file=='' or (trade_file is None):
                trade_file='graph_trade_info.pickle'
            self._dloader.dump_serialize(self.assets, self.trade, asset_file, trade_file)
