# Google Trends Data Fetcher and Exporter

Final version: **Google_Trends_v3.py**

## Description

The **Google_Trends_v3.py** python script allows you to fetch and export Google Trends data for specific keywords, timeframes, and geographical locations.
You can use it to retrieve trending keyword data and export it to CSV or Excel files.

## Prerequisites

- Python 3.x
- The following Python libraries are required and can be installed using `pip`:
  - `pandas`
  - `pytrends`
  - `argparse`
  - `json`
  - `time` (v2)

```bash
pip install pandas pytrends json argparse time
```

### Files:

- Google_Trends.py
- Google_Trends_v2.py
- **Google_Trends_v3.py**

## Usage

### Running the Script

You can run the script from the command line using the following commands:

- To fetch data:

  ```bash
  python your_script.py fetch --kw_list "Cristiano Ronaldo" --timeframe "today 5-d" --geo "UK"
  ```

  This command will fetch Google Trends data for the specified keywords, timeframe, and geographical location and print it to the console.

- To export data to CSV:

  ```bash
  python your_script.py export_csv --kw_list "Cristiano Ronaldo" --timeframe "today 5-d" --geo "UK" --filename "cr7_trends.csv"
  ```

  This command will fetch the data and export it to a CSV file with the specified filename.

- To export data to Excel:

  ```bash
  python your_script.py export_excel --kw_list "Cristiano Ronaldo" --timeframe "today 5-d" --geo "UK" --filename "cr7_trends.xlsx"
  ```

  This command will fetch the data and export it to an Excel file with the specified filename.

### Command-Line Arguments

- `--kw_list`: List of keywords (enclose in double quotes if multiple).
- `--timeframe`: Timeframe for the data (e.g., "today 5-d", "today 1-m").
- `--geo`: Geographical location (e.g., "UK", "US", leave empty for worldwide).
- `--filename`: Output filename for exporting to CSV or Excel.

### Example

Here's an example command to fetch Google Trends data for Cristiano Ronaldo in the UK for the last 5 days and export it to a CSV file:

```bash
python your_script.py fetch --kw_list "Cristiano Ronaldo" --timeframe "today 5-d" --geo "UK"
python your_script.py export_csv --kw_list "Cristiano Ronaldo" --timeframe "today 5-d" --geo "UK" --filename "cr7_trends.csv"
```

##

This library **Google_Trends_v2.py** was developed by Charilaos Sav and is open-source. Contributions are welcome.

## Version

Current version: 3

## Support

For support and inquiries, please contact me on email.

Enjoy using GoogleTrends Version 2 and 3!
