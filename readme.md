# 📊 Stock and Revenue Visualization Tool

This project demonstrates how to fetch, process, and visualize historical stock prices and revenues for companies like Tesla and GameStop using Python. 📈📉 The visualizations are created with Plotly, providing interactive and insightful graphs for analysis.

---

## 🚀 Features
- **Fetch Historical Stock Data**: Uses Yahoo Finance to retrieve stock data 📅.
- **Extract Revenue Data**: Scrapes HTML tables to obtain revenue information from provided URLs 💻.
- **Interactive Graphs**: Combines stock price and revenue data into an interactive dual-subplot visualization 📊.
- **Export as HTML**: Saves the visualizations for easy sharing and offline viewing 🌐.

---

## 📁 File Structure
```
|-- main.py            # The primary script containing all functionality
|-- requirements.txt   # Dependencies for the project
|-- README.md          # Project documentation
```

---

## 🔧 Dependencies
- `yfinance` for fetching stock data
- `pandas` for data manipulation
- `plotly` for interactive visualizations
- `requests` for web scraping
- `beautifulsoup4` for parsing HTML content


## 🛠️ Functions Explained

### 1️⃣ `make_graph(stock_data, revenue_data, stock)`
- **Purpose**: Combines historical stock prices and revenues into a dual-plot interactive graph.
- **Input**:
  - `stock_data` - Stock price data (DataFrame)
  - `revenue_data` - Revenue data (DataFrame)
  - `stock` - Stock name (string)
- **Output**: Displays the graph and saves it as an HTML file (`<stock>_revenue_graph.html`) 📂.

### 2️⃣ Tesla Stock and Revenue Processing
- **Fetch Stock Data**:
  - Uses `yfinance` to fetch historical Tesla data.
  - Resets index and prepares the DataFrame for plotting.
- **Fetch Revenue Data**:
  - Scrapes Tesla revenue data from a provided URL using `requests` and `BeautifulSoup`.
  - Cleans and processes the revenue data for visualization.

### 3️⃣ GameStop Stock and Revenue Processing
- Similar process to Tesla:
  - Stock data fetched with `yfinance`.
  - Revenue data scraped from a provided URL, cleaned, and processed.

---

## 📊 Visualization

### Tesla Graph Example
- **Top Plot**: Tesla's stock prices over time.
- **Bottom Plot**: Tesla's revenue over time.
- **Interactive**: Zoom, pan, and hover over data points for details!

### GameStop Graph Example
- Same structure as Tesla but focused on GameStop.

---

## ⚙️ How It Works
1. **Fetch Data**:
   - Stock data: `yfinance.Ticker("TSLA").history(period="max")`
   - Revenue data: Scraped from HTML tables.
2. **Clean and Process**:
   - Remove unwanted characters (e.g., `$`, `,`) from revenue data.
   - Filter rows to focus on relevant data.
3. **Visualize**:
   - Combine data using Plotly's `make_subplots`.
   - Customize layouts, titles, and interactivity.
4. **Export**:
   - Save visualizations as standalone HTML files.

---

## 📝 Example Output
### Code Execution Example:
```python
make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(gamestop_data, gamestop_revenue, 'Gamestop')
```

### Output:
- `Tesla_revenue_graph.html`
- `Gamestop_revenue_graph.html`

---

## 🌟 Key Highlights
- **User-Friendly**: Generates HTML graphs that can be opened in any browser.
- **Customizable**: Easily switch stock tickers or URLs for other companies.
- **Scalable**: Add more companies or metrics with minimal code changes.

---

## 🛡️ Disclaimer
- This project is for educational purposes only.
- Data is retrieved from public APIs and sources. Ensure compliance with data usage policies.

