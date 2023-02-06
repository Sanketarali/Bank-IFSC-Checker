import streamlit as st
import requests
import pandas as pd
from PIL import Image

def Bank_Data_Finder(IFSC_Code):
    url = 'https://ifsc.razorpay.com/' + IFSC_Code
    bank_info = requests.get(url).json()
    bank_name = bank_info['BANK']
    branch = bank_info['BRANCH']
    address = bank_info['ADDRESS']
    city = bank_info['CITY']
    state = bank_info['STATE']
    ifsc = bank_info['IFSC']
    contact = bank_info['CONTACT']
    upi = 'UPI: ' + 'Available' if bank_info['UPI'] else 'Not Available'
    rtgs = 'RTGS: ' + 'Available' if bank_info['RTGS'] else 'Not Available'
    neft = "NEFT: " + 'Available' if bank_info['NEFT'] else 'Not Available'
    imps = 'IMPS: ' + 'Available' if bank_info['IMPS'] else 'Not Available'
    return [bank_name, branch, address, city, state, ifsc, contact, upi, rtgs, neft, imps]

def run():
    img1 = Image.open('logo.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Bank IFSC Checker")
    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Warning! This data is coming from third party website, so confirm it once."</h4>''',
                unsafe_allow_html=True)
    ifsc = st.text_input('Enter your Bank IFSC Code Eg.KARB0000001')
    if st.button("Search"):
        bank_data = Bank_Data_Finder(ifsc)
        if bank_data:
            df = pd.DataFrame({'Info': bank_data},index = ['Bank Name','Branch','Address','City','State','IFSC','Contact','UPI','RTGS','NEFT','IMPS'])
            st.dataframe(df)
        else:
            st.warning("Check your IFSC code!!!")

run()
