import csv
import json
import pickle

from _internal.adts.structs import AssetNode, TradesEdge
from _internal.adts.linkedlist import LinkedList

class DataLoader:
    """
    class for loading data from api
    """
    # read csv/json
    # convert to objects
    def load_asset(self, asset_list, file_name='asset_info.csv', skip_n=1, header=True):
        if header:
            skip_n+=1
        with open(file_name) as fstream:
            _reader = csv.reader(fstream, delimiter=',')
            for row in _reader:
                if not skip_n:
                    # Do the stuff here
                    # unpacking rows
                    # Use of list here
                    _,name,sym,_,mark_cap,price,_,_,vol,*_=row
                    asset_list.insert(AssetNode(
                        name=name,
                        symbol=sym,
                        price=price,
                        volume=vol,
                        market_cap=mark_cap,
                    ))
                else:
                    skip_n-=1
        print("Total asset loaded: {0}".format(asset_list.length))
        return asset_list

    def search(self, dict_list, symbol):
        filtered_data=next((each for each in dict_list if each["symbol"] == symbol), None)
        if filtered_data:
            return filtered_data['baseAsset'],filtered_data['quoteAsset']
        else:
            return None, None

    def load_trade(self, asset_list, g, file_name='trade_info.json', token_file_name='trade_tokens.json'):
        # Algo
        # read tokens -> get base and quote assets
        # get trade info from trade_info json
        asset_list=self.load_asset(asset_list)

        with open(token_file_name) as tfn:
            # uses dict here
            token_data=json.load(tfn)
        
        with open(file_name) as fn:
            # uses dict here
            trade_data=json.load(fn)
            for each in trade_data:
                base_sym,quote_sym=self.search(token_data, each['symbol'])
                priceChangePercent,lastPrice,lastQty=each['priceChangePercent'],each['lastPrice'],each['lastQty']
                openPrice,highPrice,lowPrice=each['openPrice'],each['highPrice'],each['lowPrice']
                volume,closeTime,count=each['volume'],each['closeTime'],each['count']
                
                start=asset_list.get_item(base_sym)
                end=asset_list.get_item(quote_sym)
                
                if (not start) or (not end):
                    continue
                # Create Edge
                g.add_edge(
                    TradesEdge(
                        start=start,
                        end=end,
                        priceChangePercent=priceChangePercent,
                        lastPrice=lastPrice,
                        lastQty=lastQty,
                        openPrice=openPrice,
                        highPrice=highPrice,
                        lowPrice=lowPrice,
                        volume=volume,
                        closeTime=closeTime,
                        count=count
                    )
                )


        return asset_list,g

    def dump_serialize(self, asset_list, g):
        pickle.dump(asset_list, 'asset_list.pickle')
        pickle.dump(g, 'graph_trade_info.pickle')

    def load_serailize(self, asset_file_name='asset_list.pickle', trade_file_name='graph_trade_info.pickle'):
        asset_list = pickle.load(asset_file_name)
        g = pickle.load(trade_file_name)
        return asset_list, g
