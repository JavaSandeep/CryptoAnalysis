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
    
    def get_attribute(self, key='price'):
        if key=='price':
            return self.price
        elif key=='volume':
            return self.volume
        elif key=='market_cap':
            return self.market_cap
        else:
            return self.price


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
        Base node: {0}\nQuote node: {1}\nSymbol: {2}\nPrice Change Percent: {5}\nLast Price: {6}\nLast Quantity: {7}\nOpen Price:{8}\n
        High Price: {9}\nLow Price: {10}\nClose Time: {11}\nVolume: {3}\nCount: {4}
        """
        return template.format(
            self.start_node.get_symbol,
            self.end_node.get_symbol,
            self.symbol,
            self.volume,
            self.count,
            self.priceChangePercent,
            self.lastPrice,
            self.lastQty,
            self.openPrice,
            self.highPrice,
            self.lowPrice,
            self.closeTime
        )
    
    def get_attribute(self, key='lastPrice'):
        """
        Method to get specific attribute from the Trade nodes
        """
        if key=='volume':
            return self.volume
        elif key=='count':
            return self.count
        elif key=='priceChangePercent':
            return self.priceChangePercent
        elif key=='lastPrice':
            return self.lastPrice
        elif key=='lastQty':
            return self.lastQty
        elif key=='openPrice':
            return self.openPrice
        elif key=='highPrice':
            return self.highPrice
        elif key=='lowPrice':
            return self.lowPrice
        elif key=='closeTime':
            return self.closeTime
        else:
            return self.lastPrice

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
