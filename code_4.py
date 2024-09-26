import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

# print(sub_df1)
# print(sub_df2)
# Code complete for first example, next step is to make it case insensitive
country_code = "ARG"
year = 2012
def get_big_mac_price_by_year(year,country_code):
    query_text_country = f"(iso_a3 == '{country_code}')"
    sub_df1 = df.query(query_text_country)
    query_text_year = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    sub_df2 = sub_df1.query(query_text_year)
    return round(sub_df2['dollar_price'].mean(),2)


def get_big_mac_price_by_country(country_code):
    pass

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    print(get_big_mac_price_by_year(year,country_code))