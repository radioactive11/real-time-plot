import socketio

from scripts import plot


sio = socketio.Server(cors_allowed_origins='*')


ACTIVE_CLIENTS = []


@sio.event
def connect(sid, environ):
    print(f"[CONNECTED] {sid=}")
    ACTIVE_CLIENTS.append(sid)


@sio.event
def disconnect(sid):
    print(f"[DISCONNECTED] {sid=}")
    ACTIVE_CLIENTS.remove(sid)


@sio.event
def ping_graph(sid, data):
    symbol = data['symbol']
    print(symbol)
    
    try:
        while sid in ACTIVE_CLIENTS:
            print(f"Attempting to ping {sid=} with {symbol=}")
            graph = plot.mountain_day(symbol)
            sio.emit('graph_plot', graph, to=sid)

            sio.sleep(61)
    
    except Exception as e:
        print(f"[EXCEPTION] {e}")
    