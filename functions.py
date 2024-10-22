import numpy as np
import pandas as pd

df = pd.read_csv('files/csvs/Cleaned data zameen.csv')
df2 = pd.read_csv('files/csvs/numerical_logged.csv')

def find_distinct_values():
    purpose_distinct_values = df['purpose'].unique()
    province_distinct_values = df['province_name'].unique()
    city_distinct_values = df['city'].unique()
    property_type_distinct_values = df['property_type'].unique()
    bedroom_distinct_values = df['bedrooms'].unique()
    bath_distince_values = df['baths'].unique()
    location_distinct_values = df['location'].unique()
    area_distinct_values = df['area'].unique()
    
    return purpose_distinct_values, province_distinct_values, city_distinct_values, property_type_distinct_values, bedroom_distinct_values, bath_distince_values, location_distinct_values, area_distinct_values


def check_distinct_values():
    print(len(df['purpose'].unique()),
    len(df['province_name'].unique()),
    len(df['city'].unique()),
    len(df['property_type'].unique()),
    len(df['bedrooms'].unique()),
    len(df['baths'].unique()),
    len(df['location'].unique()),
    len(df['area'].unique()))
    
    print(len(df2['purpose'].unique()),
    len(df2['province_name'].unique()),
    len(df2['city'].unique()),
    len(df2['property_type'].unique()),
    len(df2['bedrooms'].unique()),
    len(df2['baths'].unique()),
    len(df2['location'].unique()),
    len(df2['area'].unique()))
    
if __name__ == '__main__':
    print(df.info)
    print(df2.info)
    check_distinct_values()