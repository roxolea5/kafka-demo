import numpy as np

def strategy(data):
    data['short_ma'] = data['close'].rolling(window=10).mean()
    data['long_ma'] = data['close'].rolling(window=50).mean()
    data['signal'] = 0
    data.loc[10:, 'signal'] = np.where(data.loc[10:, 'short_ma'] > data.loc[10:, 'long_ma'], 1, 0)
    data['position'] = data['signal'].diff()
    return data