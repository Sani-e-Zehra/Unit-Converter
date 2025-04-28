##Unit Converter with Streamlit
#Project 1:Build a Unit Converter with Python and Streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body{
    background-color:#000000;
    color:#ffffff;
    }
    .stApp{
    background-color:linear-gradient(135deg,#D3D3D3,#D45BFF);
    padding:30px;
    border-radius:15px;
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
    }
    h1{
      text-align:center;
      font-size:36px;
      color:#white
    }
    .stButton>button{
        background-color:#D45BFF;
        color:#ffffff;
        font-size:18px;
        padding:10px,20px;
        border-radius:8px;
        transition:background-color 0.3s ease;
        box-shadow:0 4px 6px rgba(0,0,0,0.1);
        cursor:pointer;
    }
    .stButton>button:hover{
        transform:scale(1.05);
        background:linear-gradient(45deg,#D45BFF,#D3D3D3;)
    }
    .result{
    font-size:24px;
    font-weight:bold;
    text-align:center;
    background-color:rgba(255,255,255,0.1);
    padding:20px;
    border-radius:10px;
    margin:20px;
    box-shadow:0 4px 6px rgba(0,0,0,0.1);
    }
    .footer{
        text-align:center;
        margin-top:20px;
        font-size:14px;
        color:#ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#Title
st.markdown("<h1>Unit Converter</h1>",unsafe_allow_html=True)
st.write("Easily convert between different units of measurements,lenght,weight and temprature")

#sidebar menu
conversion_type=st.sidebar.selectbox("Choose conversion type",["Length","Weight","Temperature"])
value=st.number_input("Enter value" ,value=0.0,min_value=0.0,step=0.1)
col1,col2=st.columns(2)

#length conversion
if conversion_type=="Length":
    with col1:
        from_unit=st.selectbox("From",["Meters","Kilograms","Milimeters","Miles","Feet","Yards","Inches","Centimeters","Micrometers","Nanometers"])
    with col2:
        to_unit=st.selectbox("To",["Meters","Kilograms","Milimeters","Miles","Feet","Yards","Inches","Centimeters","Micrometers","Nanometers"])
elif conversion_type=="Weight":
    with col1:
        from_unit=st.selectbox("From",["Kilograms","Grams","Milligrams","Pounds","Ounces","Tons","Stones"])
    with col2:
        to_unit=st.selectbox("To",["Kilograms","Grams","Milligrams","Pounds","Ounces","Tons","Stones"])
elif conversion_type=="Temprature":
    with col1:
        from_unit=st.selectbox("From",["Celcius","Fareinheight","Kelvin"])
    with col2:
        to_unit=st.selectbox("To",["Celcius","Fareinheight","Kelvin"])

#conversion logic
def convert_length(from_unit,to_unit,value):
    length_unit={
        'Meters':1.0,'Kilograms':0.001,'Milimeters':0.001,'Miles':1609.34,'Feet':0.3048,'Yards':0.9144,'Inches':0.0254,'Centimeters':0.01,'Micrometers':1e-6,'Nanometers':1e-9
    }
    return value*length_unit[from_unit]/length_unit[to_unit]
def convert_weight(from_unit,to_unit,value):
    weight_unit={
        'Kilograms':1.0,'Grams':0.001,'Milligrams':0.000001,'Pounds':0.453592,'Ounces':0.0283495,'Tons':1000,'Stones':6.35029
    }
    return value*weight_unit[from_unit]/weight_unit[to_unit]
    
def convert_temperature(from_unit,to_unit,value):
    if from_unit=="Celcius":
        return(value*9/5)+32 if to_unit=="Fareinheight" else value+273.15 if to_unit=="Kelvin" else value
    elif from_unit=="Fareinheight":
        return(value-32)*5/9 if to_unit=="Celcius" else value-459.67 if to_unit=="Kelvin" else value
    elif from_unit=="Kelvin":
        return value-273.15 if to_unit=="Celcius" else (value-273.15)*9/5+32 if to_unit=="Fareinheight" else value
    return value



    #button for conversion
if st.button("⏳Convert"):
    if conversion_type=="Length":
        result=convert_length(from_unit,to_unit,value)
    elif conversion_type=="Weight":
        result=convert_weight(from_unit,to_unit,value)
    elif conversion_type=="Temperature":
        result=convert_temperature(from_unit,to_unit,value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result} {to_unit}</div>",unsafe_allow_html=True)

st.markdown(f"<div class='footer'>Developed by Sani-e-Zehra <a href='https://github.com/Sani-e-Zehra/Unit-Converter.git'>Github</a></div>",unsafe_allow_html=True) 
