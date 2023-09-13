import pandas as pd
from pytrends.request import TrendReq
import time

class GoogleTrends:
    
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
    
    def get_interest_over_time(self, kw_list, timeframe='today 1-y', geo=''):
        try:
            self.pytrends.build_payload(kw_list=kw_list, timeframe=timeframe, geo=geo)
            trends_data = self.pytrends.interest_over_time()
            trends_df = pd.DataFrame(trends_data)
            return trends_df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def get_trending_keywords(self, timeframe, geo, filename):
        try:
            self.pytrends.build_payload(kw_list=[], timeframe=timeframe, geo=geo)
            trending_searches = self.pytrends.trending_searches()
            trending_searches_df = pd.DataFrame(trending_searches)
            trending_searches_df.to_csv(filename, index=False)
            return trending_searches_df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_trending_keywords_uk_5_days(self):
        return self.get_trending_keywords('now 5-d', 'GB', 'trending_keywords_uk_5_days.csv')
    
    def get_trending_keywords_worldwide_5_days(self):
        return self.get_trending_keywords('now 5-d', '', 'trending_keywords_worldwide_5_days.csv')
    
    def get_trending_keywords_worldwide_30_days(self):
        return self.get_trending_keywords('today 1-m', '', 'trending_keywords_worldwide_30_days.csv')
    
    def get_trending_keywords_worldwide_2_months(self):
        return self.get_trending_keywords('today 2-m', '', 'trending_keywords_worldwide_2_months.csv')

# Rate limit: 10 queries per second (QPS) per IP address
kw_list = ['CR7', 'Cristiano Ronaldo', "CR7_data.csv"]
gt = GoogleTrends()
interest_df = gt.get_interest_over_time(kw_list)

# Fetch trending keywords with rate limiting
trending_df_uk_5day = gt.get_trending_keywords_uk_5_days()
# Sleep for 1 seconds (10 QPS) ideally
time.sleep(1)  
trending_df_worldwide_5day = gt.get_trending_keywords_worldwide_5_days()
time.sleep(1)
trending_df_worldwide_30day = gt.get_trending_keywords_worldwide_30_days()
time.sleep(1)
trending_df_worldwide_2months = gt.get_trending_keywords_worldwide_2_months()
