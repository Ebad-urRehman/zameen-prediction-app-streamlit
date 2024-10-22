import streamlit as st
import pickle
import numpy as np
from functions import find_distinct_values
import json

# loading models and necessary files
with open('model/linear_regression_model.pkl', 'rb') as file:
    regressor = pickle.load(file)

with open('model/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
    
with open('files/categorical_to_numerical_data.json') as json_file:
    cat_to_num = json.load(json_file)

# preparing data for selecting from user
purpose_distinct_values, province_distinct_values,\
city_distinct_values, property_type_distinct_values,\
bedroom_distinct_values, bath_distince_values,\
location_distinct_values, area_distinct_values = find_distinct_values()

selected_property_type = st.selectbox('Select Property Type : ', property_type_distinct_values)
selected_city = st.selectbox('Select City : ', city_distinct_values)
selected_province = st.selectbox('Select Province : ', province_distinct_values)

selected_bedrooms = st.text_input(label='Input Custom value for bedrooms', value=3)

selected_purpose = st.selectbox('Select purpose : ', purpose_distinct_values)

with st.expander('Area'):
    selected_area = st.selectbox('Select area : ',  ['Other in Marlas', 'Other in Kanals'])
    if selected_area == 'Other in Marlas':
            selected_area = st.text_input(label='Input Custom value Area in marlas', value=5)
            selected_area = float(selected_area) * (1/1976.84) # converting to sq kms
    elif selected_area == 'Other in Kanals':
            selected_area = st.text_input(label='Input Custom value Area in Kanals', value=1)
            selected_area = float(selected_area) * (1/39536.8) # converting to sq kms

selected_baths = st.text_input(label='Input Custom value for baths', value=2)

selected_location = st.selectbox('Select Location : ', location_distinct_values)

# finding numerical values
property_value = cat_to_num['property_type'][selected_property_type]
purpose_value = cat_to_num['purpose'][f'{selected_purpose} {selected_property_type}']
city_value = cat_to_num['city'][selected_city]
province_value = cat_to_num['province_name'][selected_province]
location_value = cat_to_num['location'][selected_location]


predict_prices = st.button('Predict Price')

# user_input = [property_value, location_value, city_value, province_value, selected_baths, selected_area, purpose_value, selected_bedrooms]
user_input = [2.857516, 2.888843, 2.867222, 2.848268, 7, 0.001062, 2.867222, 6]

# scaling test values
user_input_scaled = scaler.transform([user_input])

st.info(user_input)
st.info(user_input_scaled)


# predicting price
result = regressor.predict(user_input_scaled)
st.info(result)
result = np.exp(result)
result = np.exp(result)
st.info(f'The price of house you want to buy is nearly {round(result[0], 0)} Rupees')