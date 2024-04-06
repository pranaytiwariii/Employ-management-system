import streamlit as st
import datetime
import subprocess # to open another streamlit file
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Replace 'YOUR_ENDPOINT' with your Appwrite endpoint
client.set_project('6602e2ddecc3c30aa880')  # Replace 'YOUR_PROJECT_ID' with your Appwrite project ID
client.set_key('7bc228574d7e6787fe1fec25379d819c4a8d9695da9d52e20b56c55e0f665ca97fd87a52d4581047d8c9f9cf78a8bb80996d7890eab77824ee88e3dce0c09bb09cb15da43583b5776bccadec06dde97da4ea8b8a85feba4cba6bc3d43baab82a4d716e6a7d7cbb4f5921917f788327292e63e4646e42d29bd4bf4944a1b62789')  # Replace 'YOUR_API_KEY' with your Appwrite API key

# Initialize Appwrite database service
databases = Databases(client)

# Function to add user data to the database
def add_user_data(first_name, last_name, age, emailid, password, confirmpassword):
    global document_id 
    document_id = ID.unique() # Generate a unique document ID
    data = {
        'firstname': first_name,
        'lastname': last_name,
        'age': age,
        'emailid': emailid,
        'password': password,
        'confirmpassword': confirmpassword
    }
    databases.create_document(
        database_id='6602e392c4ec44c70532',
        document_id=document_id,
        collection_id='6602e3a6c84b8fba5ec6',  # Replace 'your_collection_id' with your actual collection ID
        data=data
    )

def check_user_credentials(email, password):
    # Retrieve documents from the database
    users = databases.list_documents(database_id='6602e392c4ec44c70532', collection_id='6602e3a6c84b8fba5ec6')  # Replace with your collection ID
    for user in users['documents']:
        if user['emailid'] == email and user['password'] == password:
            return True
    return False

def chat_file():
    subprocess.Popen(["streamlit", "run", "chat.py"])
    
def main():
    st.set_page_config(page_title="JAVIS", layout="centered")
    st.markdown("<h1 style='text-align: center; color: #faca2b; font-weight: bold;'>JAVIS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>JAVIS is a free-to-use AI system. Use it for engaging conversations, gain insights, automate tasks, and witness the future of AI, all in one place.</p>", unsafe_allow_html=True)

    option = ['Sign in','Sign up']

    tabs = st.tabs(option)

    with tabs[0]:
        emailidsignin = st.text_input("Email", key="signin_email")
        passwordsignin = st.text_input("Password", type="password", key="signin_password")
        if st.button("Sign in", key="signin"):
            if check_user_credentials(emailidsignin, passwordsignin):
                st.success(f"Welcome! How was your day? How can I assist you today?")
                chat_file()
            else:
                st.error("Invalid email or password. Please try again.")
        
    with tabs[1]:
        first_name = st.text_input("First Name", key="signup_first_name")
        last_name = st.text_input("Last Name", key="signup_last_name")
        age = st.slider("Age", min_value=0, max_value=100, key="signup_age")
        emailid = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        confirmpassword = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
        if confirmpassword != password:
            st.warning("Passwords do not match. Please verify your entries.")

        if st.button("Sign up", key="signup"):
            add_user_data(first_name, last_name, age, emailid, password,confirmpassword)
            st.success(f"Welcome, {first_name}! How was your day? How can I assist you today?")
            chat_file()

    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:20px;color: #faca2b;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
