import argparse
import pandas as pd
from pytrends.request import TrendReq
import json

class GoogleTrends:
    def __init__(self, kw_list, timeframe, geo):
        self.kw_list = kw_list
        self.timeframe = timeframe
        self.geo = geo
        self.pytrends = TrendReq()
        self.trends_data = None
        self.trends_df = None

    def fetch_data(self):
        self.pytrends.build_payload(self.kw_list, timeframe=self.timeframe, geo=self.geo)
        self.trends_data = self.pytrends.interest_over_time()
        self.convert_to_dataframe()

    def convert_to_dataframe(self):
        if self.trends_data is not None:
            self.trends_df = pd.DataFrame(self.trends_data)

    def print_dataframe(self):
        if self.trends_df is not None:
            print(self.trends_df)

    def get_trending_keywords_uk_5_days(self):
        self.pytrends.build_payload(kw_list=[], timeframe='now 5-d', geo='GB')
        return self.pytrends.trending_searches(pn='united_kingdom')

    def get_trending_keywords_worldwide_5_days(self):
        self.pytrends.build_payload(kw_list=[], timeframe='now 5-d', geo='')
        return self.pytrends.trending_searches(pn='worldwide')

    def get_trending_keywords_worldwide_30_days(self):
        self.pytrends.build_payload(kw_list=[], timeframe='today 1-m', geo='')
        return self.pytrends.trending_searches(pn='worldwide')

    def get_trending_keywords_worldwide_2_months(self):
        self.pytrends.build_payload(kw_list=[], timeframe='today 2-m', geo='')
        return self.pytrends.trending_searches(pn='worldwide')

    def export_to_csv(self, filename):
        """
        Export the trend data to a CSV file.

        Args:
            filename (str): The name of the CSV file to save.
        """
        if self.trends_df is not None:
            self.trends_df.to_csv(filename, index=False)
            print(f"Data exported to {filename}")
        else:
            print("Trend data is not available. Fetch data first.")

    def export_to_excel(self, filename):
        """
        Export the trend data to an Excel file.

        Args:
            filename (str): The name of the Excel file to save.
        """
        if self.trends_df is not None:
            self.trends_df.to_excel(filename, index=False)
            print(f"Data exported to {filename}")
        else:
            print("Trend data is not available. Fetch data first.")

class GoogleTrendsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, GoogleTrends):
            # Exclude the pytrends and trends_data attributes
            return {
                'kw_list': obj.kw_list,
                'timeframe': obj.timeframe,
                'geo': obj.geo,
                'trends_df': obj.trends_df.to_dict() if obj.trends_df is not None else None
            }
        return super().default(obj)

def main():
    parser = argparse.ArgumentParser(description="Google Trends Data Fetcher and Exporter")
    parser.add_argument("action", choices=["fetch", "export_csv", "export_excel"], help="Action to perform")
    parser.add_argument("--kw_list", nargs="+", help="List of keywords")
    parser.add_argument("--timeframe", help="Timeframe for the data")
    parser.add_argument("--geo", help="Geographical location")
    parser.add_argument("--filename", help="Output filename for export")

    args = parser.parse_args()

    if args.action == "fetch":
        trends = GoogleTrends(args.kw_list, args.timeframe, args.geo)
        trends.fetch_data()
        trends.convert_to_dataframe()
        trends.print_dataframe()
    elif args.action == "export_csv":
        if args.filename:
            trends = GoogleTrends(args.kw_list, args.timeframe, args.geo)
            trends.export_to_csv(args.filename)
        else:
            print("Please provide a filename for exporting to CSV.")
    elif args.action == "export_excel":
        if args.filename:
            trends = GoogleTrends(args.kw_list, args.timeframe, args.geo)
            trends.export_to_excel(args.filename)
        else:
            print("Please provide a filename for exporting to Excel.")

if __name__ == "__main__":
    main()
