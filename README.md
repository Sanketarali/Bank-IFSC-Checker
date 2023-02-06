# Bank-IFSC-Checker
This is a Python script that uses the Razorpay IFSC API to get information about a bank using its IFSC code. It uses streamlit to create a user interface and pandas to display the data in a clean and organized manner.

# Requirements
The following packages are required to run the script:

streamlit<br>
requests<br>
pandas


You can install them by running the following command in your terminal:<br>
pip install streamlit requests pandas

# Usage
Clone the repository and run the following command:

streamlit run bank_ifsc_checker.py<br>

The script will then open a user interface in your default browser. Enter the IFSC code of the bank you want to find information about and click the "Search" button. The information will be displayed in a dataframe.

# Note: 
The data is from a third-party website, so make sure to verify the information.
