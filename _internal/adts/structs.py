#!/usr/bin/python3

# Basic units
# Graph nodes and linked list nodes are mostly same
# except for the part how they are linked to one another

class Decorators(object):
    @classmethod
    def enforce_llassetnode_datatype(cls, func):
        def wrapper(self, var):
            if type(var)!=LinkedListNode:
                print("Error. Argument passed was not of LinkedListNode data type")
                raise Exception("Invalid data type. expected LinkedListNode datatype, got "+str(type(var)))
            return func(self, var)
        return wrapper
    
    @classmethod
    def enforce_graph_assetnode_datatype(cls, func):
        def wrapper(self, var):
            if type(var)!=LinkedListAssetNode:
                print("Error. Argument passed was not of LinkedListAssetNode data type")
                raise Exception("Invalid data type. expected LinkedListAssetNode datatype, got "+str(type(var)))
            return func(self, var)
        return wrapper
    

class AssetNode:
    """
    Class implementation for generic nodes
    """
    def __init__(self, name, symbol, price=None, volume=None, market_cap=None):
        self.name=name
        self.symbol=symbol
        self.price=price
        self.volume=volume
        self.market_cap=market_cap
    
    def __str__(self):
        template="""
        Name: {0}\nSymbol: {1}\nPrice: {2}\nVolume: {3}\nMarket Cap: {4}
        """
        return (template.format(
            self.name,
            self.symbol,
            self.price,
            self.volume,
            self.market_cap
        ))
    
    @property
    def get_symbol(self):
        return str(self.symbol)


class Edge:
    """
    Class to hold edge data
    """
    start_node=None
    end_node=None

    def __init__(self, start, end):
        self.start_node=start
        self.end_node=end


class TradesEdge(Edge):
    """
    Custom edge class for the trade data
    """
    next=None
    def __init__(self, start, end, priceChangePercent=None,\
        lastPrice=None,lastQty=None,openPrice=None,highPrice=None,lowPrice=None\
            ,volume=None,closeTime=None,count=None):
        super().__init__(start=start, end=end)
        self.symbol=start.symbol+end.symbol
        self.priceChangePercent=priceChangePercent
        self.lastPrice=lastPrice
        self.lastQty=lastQty
        self.openPrice=openPrice
        self.highPrice=highPrice
        self.lowPrice=lowPrice
        self.volume=volume
        self.closeTime=closeTime
        self.count=count
    
    def __str__(self):
        template="""
        Start node: {0}\nEnd node: {1}\nSymbol: {2}\nVolume: {3}\nCount: {4}
        """
        return template.format(
            self.start_node.__str__(),
            self.end_node.__str__(),
            self.symbol,
            self.volume,
            self.count
        )

    @property
    def get_symbol(self):
        return self.symbol


class LinkedListNode:
    """
    Class implementation for linked list nodes
    """
    next = None

    def __init__(self, data_obj, n_next=None):
        self.data_obj=data_obj
        self.next = n_next
    
    def __str__(self):
        return self.data_obj.__str__()
