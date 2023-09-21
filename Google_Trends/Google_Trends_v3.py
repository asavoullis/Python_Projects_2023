import pandas as pd
from pytrends.request import TrendReq


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

    def convert_to_dataframe(self):
        self.trends_df = pd.DataFrame(self.trends_data)

    def print_dataframe(self):
        print(self.trends_df)

    def get_trending_keywords_uk_5_days(self):
        # self.pytrends.build_payload(kw_list=[], timeframe='now 5-d', geo='GB')
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


class GoogleTrends2:
    
    def __init__(self):
        self.pytrends = TrendReq()
    
    def get_interest_over_time(self, kw_list, timeframe='today 5-y', geo=''):
        self.pytrends.build_payload(kw_list=kw_list, timeframe=timeframe, geo=geo)
        trends_data = self.pytrends.interest_over_time()
        trends_df = pd.DataFrame(trends_data)
        return trends_df
    
    def get_trending_keywords_uk_5_days(self):
        self.pytrends.build_payload(kw_list=[], timeframe='now 5-d', geo='GB')
        trending_searches = self.pytrends.trending_searches(pn='united_kingdom')
        trending_searches_df = pd.DataFrame(trending_searches)
        trending_searches_df.to_csv('trending_keywords_uk_5_days.csv', index=False)
        return trending_searches_df
    
    def get_trending_keywords_worldwide_5_days(self):
        self.pytrends.build_payload(kw_list=[], timeframe='now 5-d', geo='')
        trending_searches = self.pytrends.trending_searches()
        trending_searches_df = pd.DataFrame(trending_searches)
        trending_searches_df.to_csv('trending_keywords_worldwide_5_days.csv', index=False)
        return trending_searches_df
    
    def get_trending_keywords_worldwide_30_days(self):
        self.pytrends.build_payload(kw_list=[], timeframe='today 1-m', geo='')
        trending_searches = self.pytrends.trending_searches()
        trending_searches_df = pd.DataFrame(trending_searches)
        trending_searches_df.to_csv('trending_keywords_worldwide_30_days.csv', index=False)
        return trending_searches_df
    
    def get_trending_keywords_worldwide_2_months(self):
        self.pytrends.build_payload(kw_list=[], timeframe='today 2-m', geo='')
        trending_searches = self.pytrends.trending_searches()
        trending_searches_df = pd.DataFrame(trending_searches)
        trending_searches_df.to_csv('trending_keywords_worldwide_2_months.csv', index=False)
        return trending_searches_df

# Creating an instance of GoogleTrends class
gt = GoogleTrends(kw_list=['Cristiano Ronaldo', 'CR7'], timeframe='today 1-y', geo='')

# Fetching the data
gt.fetch_data()

# Converting the data to a DataFrame
gt.convert_to_dataframe()

# Printing the DataFrame
gt.print_dataframe()

# Getting the 20 most trending keywords in the UK of the last 5 days
uk_trending_5_days = gt.get_trending_keywords_uk_5_days()
print(uk_trending_5_days)

# Getting the 20 most trending keywords worldwide of the last 5 days
worldwide_trending_5_days = gt.get_trending_keywords_worldwide_5_days()
print(worldwide_trending_5_days)

# Getting the 20 most trending keywords worldwide of the last 30 days
worldwide_trending_30_days = gt.get_trending_keywords_worldwide_30_days()
print(worldwide_trending_30_days)

# Getting the 20 most trending keywords worldwide of the last 2 months
worldwide_trending_2_months = gt.get_trending_keywords_worldwide_2_months()
print(worldwide_trending_2_months)
