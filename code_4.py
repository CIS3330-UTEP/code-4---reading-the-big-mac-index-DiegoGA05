import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')
df["iso_a3"] = df["iso_a3"].str.lower()

def get_big_mac_price_by_year(year,country_code):
    query_text_country = f"(iso_a3 == '{country_code}')"
    sub_df1 = df.query(query_text_country)
    query_text_year = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    sub_df2 = sub_df1.query(query_text_year)
    return round(sub_df2['dollar_price'].mean(),2)

def get_big_mac_price_by_country(country_code):
    query_text_country = f"(iso_a3 == '{country_code}')"
    sub_df1 = df.query(query_text_country)
    return round(sub_df1['dollar_price'].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):
    query_text_year = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    sub_df2_year = df.query(query_text_year)
    min_price_location = sub_df2_year.loc[sub_df2_year['dollar_price'].idxmin()]
    country_min = min_price_location['name']
    country_code = min_price_location['iso_a3'].upper()
    min_price = round(min_price_location['dollar_price'],2)
    return f"{country_min}({country_code}): ${min_price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query_text_year = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    sub_df2_year = df.query(query_text_year)
    max_price_location = sub_df2_year.loc[sub_df2_year['dollar_price'].idxmax()]
    country_min = max_price_location['name']
    country_code = max_price_location['iso_a3'].upper()
    max_price = round(max_price_location['dollar_price'],2)
    return f"{country_min}({country_code}): ${max_price}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(year,country_code))
    print(get_big_mac_price_by_country(country_code))
    print(get_the_cheapest_big_mac_price_by_year(year))
    print(get_the_most_expensive_big_mac_price_by_year(year))
