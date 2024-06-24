import test.cryptocoin_data_utils as cdu
import matplotlib.pyplot as plt
import ccxt

def main():
    # symbols = ['BTC-USDT']
    # klines_df = cdu.get_multiple_klines_data(symbols, bar_size= '1D', limit = 300)
    # klines_df['close'].resample('W').mean().plot(kind='line', figsize=(8, 5))
    # plt.show()

    cb = ccxt.coinbase()
    kline = cb.fetch_ohlcv('BTC/USDT', '1d')
    print(kline)

if __name__ == '__main__':
    main() 