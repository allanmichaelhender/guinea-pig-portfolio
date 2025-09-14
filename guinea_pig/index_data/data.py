from urllib.request import urlopen
import json

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

datefrom = "2024-01-01"
dateto = "2025-01-01"
apikey="xjDy6auzJiNBaXQjmERBIGb84lN93EsR"

def create_url(symbol,datefrom,dateto,apikey):
    return "https://financialmodelingprep.com/stable/historical-price-eod/full?" + f"apikey={apikey}" + f"&from={datefrom}" + f"&to={dateto}" + f"&symbol={symbol}"
    
    
FTSE_url = create_url('^FTSE',datefrom,dateto,apikey)
SNP500_url = create_url('^GSPC',datefrom,dateto,apikey)


FTSE_data_raw = get_jsonparsed_data(FTSE_url)
SNP500_data_raw = get_jsonparsed_data(SNP500_url)

def create_list_of_data(data):
    data_tuples = []
    for x in data:
        new_row = (x['date'], x['open'], x['high'], x['low'], x['close'], x['volume'], x['change'], x['changePercent'])
        data_tuples.append(new_row)
    return data_tuples

FTSE_data = create_list_of_data(FTSE_data_raw)
SNP500_data = create_list_of_data(SNP500_data_raw)

