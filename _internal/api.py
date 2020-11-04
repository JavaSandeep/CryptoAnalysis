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
                print(self.assets)
            elif option_2==2:
                # get the file name
                f_name,*_=args
                self.assets=self._dloader.load_asset(LinkedList())
                if f_name=='' or (f_name is None):
                    _,self.trade=self._dloader.load_trade(self.assets, g=Graph())
                else:
                    _,self.trade=self._dloader.load_trade(self.assets, g=Graph(), file_name=f_name)
                print(self.trade)
            elif option_2==3:
                f_name,*_=args
                if f_name=='' or (f_name is None):
                    self.assets, self.trade=dloader.load_serailize()
                else:
                    self.assets, self.trade=dloader.load_serailize(trade_file_name=f_name)
                print(self.trade)
        elif option_1==2:
            f_name,*_=args
            asset=self.trade.vertices.get_item(f_name)
            print(asset)
        elif option_1==3:
            f_name,*_=args
            trade=self.trade.edges.get_item(f_name)
            print(trade)
        elif option_1==4:
            source, dest=args
            self.trade.dfs(
                self.trade.vertices.find(source),
                self.trade.vertices.find(dest),
                LinkedList(),
                LinkedList()
            )
            print("Number of paths found: {0}".format(self.trade.list_paths.length))
        elif option_1==5:
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
                print(sorted.get_index(i))

            sorted=self.trade.vertices.sort(key='price')
            print("Lowest 10 assets based on their price")
            for i in range(10):
                print(sorted.get_index(i))

            sorted=self.trade.vertices.sort(key='volume', inverse=True)
            print("Top 10 assets based on their volume")
            for i in range(10):
                print(sorted.get_index(i))


            sorted=self.trade.vertices.sort(key='market_cap', inverse=True)
            print("Top 10 assets based on their market cap")
            for i in range(10):
                print(sorted.get_index(i))
        elif option_1==7:
            # Description of trade
            print("Statistics on trades based on different properties")
            sorted=self.trade.edges.sort(key='lastPrice', inverse=True)
            print("Top 10 trades based on their last price")
            for i in range(10):
                print(sorted.get_index(i))

            sorted=self.trade.edges.sort(key='lastPrice')
            print("Lowest 10 trades based on their last price")
            for i in range(10):
                print(sorted.get_index(i))

            sorted=self.trade.edges.sort(key='volume', inverse=True)
            print("Top 10 assets based on their volume")
            for i in range(10):
                print(sorted.get_index(i))


            sorted=self.trade.edges.sort(key='count', inverse=True)
            print("Top 10 assets based on their count")
            for i in range(10):
                print(sorted.get_index(i))
            
            sorted=self.trade.edges.sort(key='count')
            print("Top 10 assets based on their count")
            for i in range(10):
                print(sorted.get_index(i))
        elif option_1==8:
            f_name,*_=args
            if f_name=='' or (f_name is None):
                self.assets, self.trade=dloader.dump_serailize()
            else:
                self.assets, self.trade=dloader.dump_serailize(self.assets, self.trade)

        