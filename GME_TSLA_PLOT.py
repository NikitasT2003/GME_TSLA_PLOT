import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
import plotly.io as pio
import requests
from bs4 import BeautifulSoup

pio.renderers.default = 'browser'  # Change to 'browser' if 'vscode' doesn't work

# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True,
        subplot_titles=("Historical Share Price", "Historical Revenue"),
        vertical_spacing=0.3
    )

    #
    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']

   
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data_specific['Date']),
            y=stock_data_specific['Close'].astype(float),
            name="Share Price"
        ),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(revenue_data_specific['Date']),
            y=revenue_data_specific['Revenue'].astype(float),
            name="Revenue"
        ),
        row=2, col=1
    )

    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)

    
    fig.update_layout(
        showlegend=False,
        height=900,
        title=stock,
        xaxis_rangeslider_visible=True
    )
    fig.show()
    fig.write_html(f"{stock}_revenue_graph.html")



# Fetch Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head())


url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data , 'html.parser')
dataframe = pd.DataFrame(columns = ["Date" , "Revenue"])


table = soup.find_all("tbody")[1]

tesla_revenue = pd.DataFrame(columns=["Date","Revenue"])
for row in table.find_all("tr"):
    cols = row.find_all("td")
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()



    tesla_revenue = pd.concat([tesla_revenue,pd.DataFrame({"Date":[date],"Revenue":[revenue]})], ignore_index = True )
  

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r'[\$,]', '', regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.tail()




gamestop = yf.Ticker("GME")
gamestop_data = gamestop.history(period="max")
gamestop_data.reset_index(inplace=True)
print(gamestop_data.head())

url2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
response2 = requests.get(url2)
html_data2 = response.text

soup2 = BeautifulSoup(html_data2 , 'html.parser')
dataframe2 = pd.DataFrame(columns = ["Date" , "Revenue"])

table2 = soup.find_all("tbody")[1]

gamestop_revenue = pd.DataFrame(columns=["Date","Revenue"])
for row in table2.find_all("tr"):
    cols = row.find_all("td")
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()



    gamestop_revenue = pd.concat([gamestop_revenue,pd.DataFrame({"Date":[date],"Revenue":[revenue]})], ignore_index = True )
  

gamestop_revenue["Revenue"] = gamestop_revenue['Revenue'].str.replace(r'[\$,]', '', regex=True)
gamestop_revenue.dropna(inplace=True)
gamestop_revenue = gamestop_revenue[gamestop_revenue['Revenue'] != ""]
gamestop_revenue.tail()




make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(gamestop_data, gamestop_revenue, 'Gamestop')
