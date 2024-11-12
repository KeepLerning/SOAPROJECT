import yfinance as yf
import requests
import os

def get_usd_to_idr_rate():
    # API key dari environment variable atau default key jika tidak ada
    api_key = os.getenv('EXCHANGE_RATE_API_KEY', 'd36eee9bd214d4788bfcb2c5')  
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Ini akan memicu exception jika status code bukan 200
        data = response.json()
        return data['conversion_rates'].get('IDR')
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch exchange rate. {e}")
        return None


def get_stock_data(symbol,stock_id=None):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1y")  # Retrieve data for the past year

        if not data.empty:
            # Current price (latest close price)
            price_in_usd = data['Close'].iloc[-1]
            
            # Calculating price changes
            price_1d = data['Close'].iloc[-2] if len(data) > 1 else price_in_usd
            price_1w = data['Close'].iloc[-6] if len(data) > 6 else price_in_usd
            price_1m = data['Close'].iloc[-21] if len(data) > 21 else price_in_usd
            price_1y = data['Close'].iloc[0] if len(data) > 250 else price_in_usd
            
            # Calculate percentage changes
            change_1d = ((price_in_usd - price_1d) / price_1d) * 100 if price_1d != 0 else 0
            change_1w = ((price_in_usd - price_1w) / price_1w) * 100 if price_1w != 0 else 0
            change_1m = ((price_in_usd - price_1m) / price_1m) * 100 if price_1m != 0 else 0
            change_1y = ((price_in_usd - price_1y) / price_1y) * 100 if price_1y != 0 else 0

            # Additional stock info
            market_cap = stock.info.get('marketCap', 'Tidak tersedia')
            high_52_week = stock.info.get('fiftyTwoWeekHigh', 'Tidak tersedia')
            low_52_week = stock.info.get('fiftyTwoWeekLow', 'Tidak tersedia')

            return {
                'current_price': round(price_in_usd, 2),
                'market_cap': market_cap,
                'high_52_week': high_52_week,
                'low_52_week': low_52_week,
                'change_1d': round(change_1d, 2),
                'change_1w': round(change_1w, 2),
                'change_1m': round(change_1m, 2),
                'change_1y': round(change_1y, 2)
            }
        else:
            print(f"Data saham untuk simbol {symbol} tidak tersedia.")
            return None
    except Exception as e:
        print(f"Error: Tidak dapat mengambil data saham. {e}")
        return None