# Data-Cleaning
## Python scripts for aggregating, validating, and transforming files

---
### General-Purpose

 *under construction* 
 
---
### Stock Data Package:
- applies to csv files
- headers: Ticker, Date, Low, Open, Volume, High, Close, Adjusted Close

**Aggregate.py** 
- combines csv files with provided file pathes
- searches folders and combines csv files from different directories

**Validate.py**
- identifies the number of unique stock tickers, abnormal data,
- creates csv of abnormal data grouped by ticker and prints to terminal a list of tickers with abnormal data  

**Transform.py**
- Removes all abnormal stock ticker data and creates a new cleansed csv






