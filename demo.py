from pytrends.request import TrendReq

pytrends = TrendReq(hl="en-US", tz=360)

# keywords to search for
kw_list = ["Data science"]
pytrends.build_payload(kw_list, cat=0, timeframe="today 5-y", geo="", gprop="")

# dataframe
time_df = pytrends.interest_over_time()

print(time_df.head())
