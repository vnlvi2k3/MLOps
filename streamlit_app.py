import streamlit as st 
import pickle

LATITUDE = 40.71422708323266
LONGITUDE = -73.94160121297645

st.title('New York Housing Price Prediction')
st.write('This is a simple web app to predict the price of a house in New York City based on its size in square feet and the number of bedrooms.')

@st.cache_resource
def load_model():
    with open('rf_regressor.pkl', 'rb') as f:
        return pickle.load(f)
    
model = load_model()

#['BEDS', 'BATH', 'PROPERTYSQFT', 'LATITUDE', 'LONGITUDE']
def predict(beds, bath, property):
    X = [[beds, bath, property, LATITUDE, LONGITUDE]]
    return model.predict(X)[0]

beds = st.slider('Beds', 1, 50, 3)
bath = st.number_input('Bath', 0, 50, 2)
prop = st.number_input('Property Sqft', 230, 10000, 2000)

if st.button("Predict Price"):
    result = predict(beds, bath, prop)
    st.write('The estimated price of the house is $', result)

    
