import datetime
import time
import random
import ccxt
import pandas as pd

bought =  {}

currency = 'USDT'
no_of_time_profit = 0
no_of_time_loss = 0
last_price = {}
#API credentials
api_key = '<Add your API Key from Binance>'
api_secret = '<Add your API secret from Binance>'
capital = 100
per_trade_capital = 20.0
pnl = 0
trading_fee = .2
take_profit_percentage = 2
stop_loss_percentage = -20

exchange = ccxt.binance(
    {
        'apiKey': api_key,
        'secret': api_secret,
        'options': {
            'createMarketBuyOrderRequiresPrice': False, # switch off
        },
    }
)

# avoid low volumes
symbols = [
    '1000SATS',
    '1000CAT',
    '1INCH',
    '1MBABYDOGE',
    'AAVE',
    'ACA',
    'ACE',
    'ACH',
    'ACM',
    'ACT',
    'ACX',
    'ADA',
    'ADX',
    'AERGO',
    'AEUR',
    'AEVO',
    'AGLD',
    'AI',
    'AKRO',
    'ALCX',
    'ALGO',
    'ALICE',
    'ALPACA',
    'ALPHA',
    'ALPINE',
    'ALT',
    'AMB',
    'AMP',
    'ANKR',
    'APE',
    'API3',
    'APT',
    'ARB',
    'ARDR',
    'ARKM',
    'ARK',
    'ARPA',
    'AR',
    'ASR',
    'ASTR',
    'AST',
    'ATA',
    'ATM',
    'ATOM',
    'AUCTION',
    'AUDIO',
    'AVA',
    'AVAX',
    'AXL',
    'AXS',
    'BADGER',
    'BAKE',
    'BAL',
    'BANANA',
    'BAND',
    'BAR',
    'BAT',
    'BB',
    'BCH',
    'BEAMX',
    'BEL',
    'BETA',
    'BICO',
    'BIFI',
    'BLUR',
    'BLZ',
    'BNB',
    'BNSOL',
    'BNT',
    'BNX',
    'BOME',
    'BONK',
    'BSW',
    'BTC',
    'BTTC',
    'BURGER',
    'C98',
    'CAKE',
    'CATI',
    'CELO',
    'CELR',
    'CETUS',
    'CFX',
    'CHESS',
    'CHR',
    'CHZ',
    'CITY',
    'CKX',
    'CKV',
    'COMBO',
    'COMP',
    'COS',
    'COTI',
    'COW',
    'CREAM',
    'CRV',
    'CTK',
    'CTSI',
    'CTXC',
    'CVC',
    'CVX',
    'CYBER',
    'DAR',
    'DASH',
    'DATA',
    'DCR',
    'DEGO',
    'DENT',
    'DEXE',
    'DF',
    'DGB',
    'DIA',
    'DODO',
    'DOGE',
    'DOGS',
    'DOT',
    'DUSK',
    'DYDX',
    'DYM',
    'EDU',
    'EGLD',
    'EIGEN',
    'ELF',
    'ENA',
    'ENJ',
    'ENS',
    'EOS',
    'ERN',
    'ETC',
    'ETHFI',
    'ETH',
    'FARM',
    'FET',
    'FIDA',
    'FIL',
    'FIO',
    'FIRO',
    'FIS',
    'FLM',
    'FLOKI',
    'FLOW',
    'FLUX',
    'FORTH',
    'FTM',
    'FTT',
    'FUN',
    'FXS',
    'GALA',
    'GAS',
    'GHST',
    'GLMR',
    'GLM',
    'GMT',
    'GMX',
    'GNO',
    'GNS',
    'GRT',
    'GTC',
    'G',
    'HARD',
    'HBAR',
    'HFT',
    'HIFI',
    'HIGH',
    'HIVE',
    'HMSTR',
    'HOOK',
    'HOT',
    'ICP',
    'ICX',
    'IDEX',
    'ID',
    'ILV',
    'IMX',
    'INJ',
    'IOST',
    'IOTA',
    'IOTX',
    'IO',
    'IQ',
    'IRIS',
    'JASMY',
    'JOE',
    'JST',
    'JTO',
    'JUP',
    'JUV',
    'KAIA',
    'KAVA',
    'KDA',
    'KEY',
    'KMD',
    'KNC',
    'KSM',
    'LAZIO',
    'LDO',
    'LEVER',
    'LINA',
    'LINK',
    'LISTA',
    'LIT',
    'LOKA',
    'LPT',
    'LQTY',
    'LRC',
    'LSK',
    'LTC',
    'LTO',
    'LUMIA',
    'LUNA',
    'LUNC',
    'MAGIC',
    'ME',
    'MOVE',
    'MANA',
    'MANTA',
    'MASK',
    'MAV',
    'MBL',
    'MBOX',
    'MDT',
    'MEME',
    'METIS',
    'MINA',
    'MKR',
    'MLN',
    'MOVR',
    'MTL',
    'NEAR',
    'NEIRO',
    'NEO',
    'NEXO',
    'NFP',
    'NKN',
    'NMR',
    'NOT',
    'NTRN',
    'NULS',
    'OAX',
    'OGN',
    'OG',
    'OMNI',
    'OM',
    'ONE',
    'ONG',
    'ONT',
    'OP',
    'ORCA',
    'ORDI',
    'OSMO',
    'OXT',
    'PAXG',
    'PDA',
    'PENDLE',
    'PENGU',
    'PEOPLE',
    'PEPE',
    'PERP',
    'PHA',
    'PHB',
    'PIVX',
    'PIXEL',
    'PNUT',
    'POL',
    'POLYX',
    'POND',
    'PORTAL',
    'PORTO',
    'POWR',
    'PROM',
    'PROS',
    'PSG',
    'PUNDIX',
    'PYR',
    'PYTH',
    'QI',
    'QKC',
    'QNT',
    'QTUM',
    'QUICK',
    'RAD',
    'RARE',
    'RAY',
    'RDNT',
    'REI',
    'RENDER',
    'REN',
    'REQ',
    'REZ',
    'RIF',
    'RLC',
    'RONIN',
    'ROSE',
    'RPL',
    'RSR',
    'RUNE',
    'RVN',
    'SAGA',
    'SAND',
    'SANTOS',
    'SCRT',
    'SCR',
    'SC',
    'SEI',
    'SFP',
    'SHIB',
    'SKL',
    'SLF',
    'SLP',
    'SNT',
    'SNX',
    'SOL',
    'SPELL',
    'SSV',
    'STEEM',
    'STG',
    'STMX',
    'STORJ',
    'STPT',
    'STRAX',
    'STRK',
    'STX',
    'SUI',
    'SUN',
    'SUPER',
    'SUSHI',
    'SXP',
    'SYN',
    'SYS',
    'TAO',
    'TFUEL',
    'THETA',
    'THE',
    'TIA',
    'TKO',
    'TLM',
    'TNSR',
    'TON',
    'TRB',
    'TROY',
    'TRU',
    'TRX',
    'TURBO',
    'T',
    'TWT',
    'UFT',
    'UMA',
    'UNI',
    'USUAL',
    'USTC',
    'UTK',
    'VANRY',
    'VANA',
    'VELDOROME',
    'VET',
    'VIB',
    'VIC',
    'VIDT',
    'VITE',
    'VOXEL',
    'VTHO',
    'WAN',
    'WAXP',
    'WBETH',
    'WBTC',
    'WIF',
    'WING',
    'WIN',
    'WLD',
    'WOO',
    'WRX',
    'W',
    'XAI',
    'XEC',
    'XLM',
    'XNO',
    'XRP',
    'XTZ',
    'XVG',
    'XVS',
    'YFI',
    'YGG',
    'ZEC',
    'ZEN',
    'ZIL',
    'ZK',
    'ZRO',
    'ZRX',
]
timeframe = '1m'

# retuns bool, price, ratio
# returns true -> buy, false -> sell
def paper_trading(symbol):
    try:
        data = exchange.fetch_ohlcv(symbol, timeframe)
    except:
        return False, 0,0
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    df['ma'] = df['close'].rolling(window=15).mean()

    if df['close'].iloc[-1] > df['ma'].iloc[-1]:
        return True, df['close'].iloc[-1], df['close'].iloc[-1]/df['ma'].iloc[-1]
    elif df['close'].iloc[-1] < df['ma'].iloc[-1]:
        return False, df['close'].iloc[-1], df['close'].iloc[-1] / df['ma'].iloc[-1]

def btcInBuy(toBuy):
    for b in toBuy:
        if b[0] == 'BTC/' + currency:
            return True
    return False

if __name__ == '__main__':
    while True:
        toBuy = []
        toSell = []

        #read data
        for s in symbols:
            sym = s + '/' + currency

            try:
                buy, price, ratio = paper_trading(sym)
            except:
                continue
            if sym in bought:
                b = bought[sym]
                boughtUnit, boughtPrice = b[0], b[1]
                possible_profit_ratio = ((float(price) - float(boughtPrice)) / float(boughtPrice)) * 100
                print(datetime.datetime.now(), ' coin %s profit ratio is %s' % (sym, possible_profit_ratio))

            if not buy and ratio == 0:
                toSell.append((sym, price, ratio, False))
            elif buy:
                toBuy.append((sym, price, ratio))
                toSell.append((sym, price, ratio, False))
            else:
                toSell.append((sym, price, ratio, True))

        toBuy.sort(key=lambda tup: tup[2], reverse=True)
        toSell.sort(key=lambda tup: tup[2])
        print(datetime.datetime.now()," tobuy ", toBuy)
        print(datetime.datetime.now()," tosell ", toSell)

        for c in toBuy:
            if capital <= 0:
                break
            coin, price = c[0], c[1]
            try:
                d = exchange.fetch_ohlcv(coin, timeframe)
            except:
                continue
            d_details = pd.DataFrame(d, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            cur_price = float(d_details['close'].iloc[-1])
            if cur_price > 1.001*price:
                continue
            price = cur_price

            allocated_capital = min(capital, per_trade_capital)

            unit = allocated_capital/price

            print(datetime.datetime.now(), ' executing buy order of %s for euro %s' % (coin, allocated_capital))
            try:
                order = exchange.create_market_buy_order(coin, unit)
            except Exception as error:
                print(datetime.datetime.now(), ' error while executing buy order of %s for euro %s: %s' % (coin, allocated_capital, error))
                continue
            p = order['info']['fills'][0]['price']
            u = float(order['info']['executedQty'])*.999

            print(datetime.datetime.now(), ' executed buy order of %s for euro %s: %s' %(coin, allocated_capital, order))
            print(datetime.datetime.now(), " buying %s with eur %s, unit %s"%(coin, allocated_capital, unit))
            if coin not in bought:
                bought[coin] = (float(u), float(p))
            else:
                bc = bought[coin]
                old_u = bc[0]
                old_p = bc[1]
                new_u = old_u + float(u)
                new_p = (old_u * old_p + float(u) * float(p)) / (old_u + float(u))
                bought[coin] = (float(new_u), float(new_p))
            print(datetime.datetime.now(), " bought =", bought)
            capital-=allocated_capital
            last_price[coin] = price

        for c in toSell:
            if len(bought) == 0:
                break
            coin, price, must_sell = c[0], c[1], c[3]
            if coin not in bought:
                continue

            # check if price drop in between
            try:
                d = exchange.fetch_ohlcv(coin, timeframe)
            except:
                continue
            d_details = pd.DataFrame(d, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            cur_price = float(d_details['close'].iloc[-1])
            if cur_price < 0.999 * price:
                continue
            price = cur_price

            b = bought[coin]
            boughtUnit, boughtPrice = b[0], b[1]
            possible_profit_ratio = ((float(price) - float(boughtPrice))/float(boughtPrice))*100
            print(datetime.datetime.now(), ' coin %s profit ratio is %s' % (coin, possible_profit_ratio))

            # don't take more than stop_loss_percentage loss
            # if we are getting > take_profit_percentage profit -> sell
            if possible_profit_ratio > stop_loss_percentage and possible_profit_ratio < take_profit_percentage:
                continue

            print(datetime.datetime.now(), ' executing sell order of %s unit %s' % (coin, boughtUnit))
            try:
                order = exchange.create_market_sell_order(coin, boughtUnit)
            except Exception as error:
                print(datetime.datetime.now(), ' error executing sell order of %s unit %s: %s' % (coin, boughtUnit, error))
                continue

            soldUnit = float(order['info']['executedQty'])
            soldPrice = price

            print(datetime.datetime.now(), ' executed sell order of %s unit %s: %s' % (coin, soldUnit, order))
            print(datetime.datetime.now(), " selling %s getting eur %s, unit %s" % (coin, soldUnit*soldPrice, soldUnit))
            del bought[coin]
            print(datetime.datetime.now(), " bought =", bought)
            capital += (soldUnit*soldPrice*.995)
            pnl += ((soldUnit*(soldPrice - boughtPrice))*.995)
            last_price[coin] = price

            if soldPrice > boughtPrice:
                no_of_time_profit+=1
            else:
                no_of_time_loss+=1


        print(datetime.datetime.now(), "***")
        print("pnl = ", pnl)
        print("capital = ", capital)
        print("bought = ", bought)
        print("profit_no= ", no_of_time_profit)
        print("loss_no= ", no_of_time_loss)
        print("***")
        time.sleep(60)
