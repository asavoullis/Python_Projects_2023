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

# Creating an instance of GoogleTrends class
CR7 = GoogleTrends(kw_list=['Cristiano Ronaldo', 'CR7'], timeframe='today 5-d', geo='UK')

# Fetch data and convert it to a DataFrame
CR7.fetch_data()
CR7.convert_to_dataframe()
CR7.print_dataframe()

# Getting the 20 most trending keywords in the UK of the last 5 days
uk_trending_5_days = CR7.get_trending_keywords_uk_5_days()

# Export the data to a CSV file
CR7.export_to_csv('cr7_trends.csv')

# Export the data to an Excel file
CR7.export_to_excel('cr7_trends.xlsx')

# Getting the 20 most trending keywords worldwide of the last 5 days
worldwide_trending_5_days = CR7.get_trending_keywords_worldwide_5_days()
print(worldwide_trending_5_days)

# Getting the 20 most trending keywords worldwide of the last 30 days
worldwide_trending_30_days = CR7.get_trending_keywords_worldwide_30_days()
print(worldwide_trending_30_days)

# Getting the 20 most trending keywords worldwide of the last 2 months
worldwide_trending_2_months = CR7.get_trending_keywords_worldwide_2_months()
print(worldwide_trending_2_months)
