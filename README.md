# Sports Betting Arbitrage Automation

This project automates the process of fetching sports betting odds from an API, saving them into text files, converting these data into Excel format, and finally checking for arbitrage opportunities. The project is divided into three main Python scripts:

1. **`concurrentfetchapi.py`**
2. **`coccurrentexcelmaker.py`**
3. **`arbitragecheckercoccurent.py`**

## Prerequisites

Before running the scripts, ensure you have the following installed:

- **Python 3.x**: Download and install Python from [python.org](https://www.python.org/downloads/).

- **Required Python packages**: You will need the following packages:
  - `requests`: For making HTTP requests to the betting odds API.
  - `pandas`: For data manipulation and saving to Excel.
  - `xlsxwriter`: For writing data to Excel files.

You can install the required packages using pip. Open your terminal or command prompt and run:

```bash
pip install requests pandas xlsxwriter
