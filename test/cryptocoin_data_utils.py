import requests
import pandas as pd
import warnings

pd.set_option('expand_frame_repr', False)
warnings.simplefilter("ignore", category=FutureWarning)

def get_single_kline_data(symbol, bar_size = "1H", limit = 300):
    # max limit is 300
    kline_url = 'https://www.okx.com/api/v5/market/candles?instId={}&bar={}&limit={}'.format(symbol, bar_size, limit)
    res_obj = requests.get(kline_url)
    if res_obj.status_code != 200:
        print("Error happens when requesting single kline data. Status code: {}".format(res_obj.status_code))
        return None
    
    json_obj = res_obj.json()
    if json_obj['code'] != '0':
        print("Error happens in the single kline json object. Error code: {}".format(json_obj['code']))
        return None
        
    raw_df = pd.DataFrame(json_obj['data'])
    kline_df = raw_df.copy()
    kline_df.columns = ['datetime', 'open', 'high', 'low', 'close', 'vol', 'vol_ccy', 'vol_ccy_quote', 'complete']
    kline_df['datetime'] = pd.to_datetime(kline_df['datetime'], unit='ms')
    kline_df['symbol'] = symbol

    # Reformat
    kline_df.set_index('datetime', inplace=True)
    kline_df['open'] = kline_df['open'].astype(float)
    kline_df['high'] = kline_df['high'].astype(float)
    kline_df['low'] = kline_df['low'].astype(float)
    kline_df['close'] = kline_df['close'].astype(float)
    kline_df['vol'] = kline_df['vol'].astype(float)
    kline_df['vol_ccy'] = kline_df['vol_ccy'].astype(float)
    kline_df['vol_ccy_quote'] = kline_df['vol_ccy_quote'].astype(float)
    kline_df['complete'] = kline_df['complete'].astype(int)

    if kline_df.index.duplicated().any():
        print("Dedup for symbol: {}".format(symbol))
        kline_df = kline_df[~kline_df.index.duplicated()]
    
    return kline_df
        
def get_multiple_klines_data(symbols, bar_size = '1H', limit = 300):
    klines_df = pd.DataFrame()
    for symbol in symbols:
        kline_df = get_single_kline_data(symbol, bar_size, limit)
        if klines_df is None:
            continue
        klines_df = pd.concat([klines_df, kline_df])

    return klines_df