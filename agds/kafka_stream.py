import websocket
from confluent_kafka import Producer

def on_message(ws, message):
    # Assuming the message is in JSON format
    # Modify this part according to the actual message format
    producer.produce('finnhub', key=None, value=message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    
    # Kafka Producer Configuration
    producer_conf = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(producer_conf)
    
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=clnsdnhr01qqp7jpdfdgclnsdnhr01qqp7jpdfe0",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
