import pandas as pd
from pytrends.request import TrendReq

class GoogleTrends:
    
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



kw_list = ['CR7', 'Cristiano Ronaldo']
gt = GoogleTrends()
interest_df = gt.get_interest_over_time(kw_list)
trending_df_uk_5day = gt.get_trending_keywords_uk_5_days()
