# daily_flash_report

**daily_flash_report** is an autonomous Python-based tool designed for daily financial analysis using exclusively open-source data sources. The project aims to provide a quick and comprehensive snapshot of key financial market data, enabling users to stay informed on daily market movements, top performers, and major economic indicators.

## Project Overview

**daily_flash_report** generates a daily report with key insights across several financial data categories, divided into four main sections:

### Part 1: Daily Return of Major Stock Market Indexes
This section tracks the daily performance of major stock market indexes, allowing users to observe and compare return fluctuations across global markets.  
- **Source**: Yahoo Finance

### Part 2: Top 10 Best and Worst Daily Performers
Highlights the top 10 best and worst daily performers across three major equity indices: S&P 500, Nasdaq 100, and Eurostoxx 50. This breakdown is useful for identifying outperforming and underperforming stocks within these key markets.  
- **Source**: Yahoo Finance

### Part 3: Central Banks Policy Rates and Sovereign 10-Year Bond Yields
This section includes visualizations of central banks’ policy rates and 10-year sovereign bond yields, which provide insights into global monetary policy trends and government borrowing costs.  
- **Source**: Federal Reserve Bank of St. Louis (FRED)

### Part 4: Daily Returns of Main Commodities and FX
Reports daily returns for major commodities and foreign exchange (FX) rates, helping users track shifts in these critical asset classes.  
- **Source**: Yahoo Finance

## Getting Started

1. **Prerequisites**: Ensure you have Python installed and the required libraries (e.g., `yfinance`, `pandas`, `matplotlib` and ‘pandas_datareader’) available.
2. **Installation**: Clone the repository and install dependencies as outlined in `requirements.txt`.
3. **Running the Tool**: Execute the main script to generate the daily report, which will output the latest financial data for each section.

## Deployment

The application is deployed on Render for cloud accessibility. For more details, please refer to the cloud deployment instructions provided in the repository.

## Feedback and Contributions

Feedback is welcome to enhance and expand the tool's functionalities. To contribute to the project, please submit issues or pull requests via GitHub.

For more technical details, check out the source code available in the GitHub repository.
