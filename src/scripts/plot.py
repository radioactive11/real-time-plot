#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
from plotly.io import to_json



def mountain_day(symbol: str) -> dict:
    stocks = ["RELIANCE.NS"]
    data = yf.download(tickers=stocks, period='1d', interval='1m')

    if data.iloc[-1]["Close"] < data.iloc[-2]["Close"]:
        area_color = "red"

    elif data.iloc[-1]["Close"] == data.iloc[-2]["Close"]:
        area_color = "yellow"

    else:
        area_color = "lime"

    ymin = data['High'].min()
    ymax = data['High'].max()
    area = go.Figure(go.Scatter(x=data.index, y=data['High'], fill='tozeroy', mode='lines', line_color=area_color), 
                    layout_yaxis_range=[ymin-5, ymax+5])

    area.update_xaxes(
        yaxis_title='Stock Price (₹)',  
        rangeslider_visible=True,
        rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward",),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ]),
        bgcolor='black')
    )
    area.update_layout(template='plotly_dark')

    graph = to_json(area)
    return graph


