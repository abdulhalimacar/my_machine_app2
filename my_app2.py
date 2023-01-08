import streamlit as st
import pickle
import pandas as pd 


filename = "my_model4"
model = pickle.load(open(filename,'rb'))


car_model = st.sidebar.radio("select your car model", ['Audi A3', 'Audi A1', 'Opel Astra', 'Opel Insignia', 'Opel Corsa','Renault Clio', 'Renault Espace', 'Renault Duster'])
hp_kW = st.sidebar.slider("what is horsepower of your car?",40,239,step=1)
Displacement_cc = st.sidebar.slider("what is displacement of your car in cc?",890,2967,step=1)
km = st.sidebar.slider("at what km is your car?",0,317000,step=1)
age = st.sidebar.selectbox("what is the age of your car?", (0,1,2,3))
Gearing_Type = st.sidebar.radio("select gearing type of your car",('Manual', 'Automatic', 'Semi-automatic'))
cons_comb = st.sidebar.slider("what is consumption of your car?",3,10,step=1)


my_dict = {
        "car_model":car_model,
        "hp_kW":hp_kW,
        "Displacement_cc":Displacement_cc,
        "km":km,
        "age":age,
        "Gearing_Type":Gearing_Type, 
        "cons_comb":cons_comb
}

data = pd.DataFrame.from_dict([my_dict])


st.header('the configuration of your car:')

st.table(data)

if st.button("predict"):
    pred = model.predict(data)
    st.write(pred[0])
