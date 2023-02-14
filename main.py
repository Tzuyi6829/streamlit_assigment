 # Imports required ---
import streamlit as st #nickname
import sqlite3 as sqlite #squlite: database
import pandas as pd #operation 

#Instructions:
#go in Shell (on the right)
#write "pip install --upgrade streamlit"
#launch with "streamlit run main.py"

#function enables the code to avoid running from the top to the bottom everytime
@st.cache_data 
def get_data():
  con = sqlite.connect("Fake_sales_data.db") #connect to the database file
  data = pd.read_sql_query("SELECT * from SalesA",con) # fetching the data from salesA table 
  return data 
data=get_data() #call the function to get the value, vlaue in "data"

st.title('Sales Dashboard') #create the title in website 

st.write(f"We have {len(data)} datapoints") #WHY????? #st.write: to add a caption below 

choice = st.selectbox('Select a Company', data["company"].unique(), index=0)
#unique: equals to "distinct" in sql
#choice: variable (the one selected)

#errors everywhere hehe

new_data=data[data["company"]== choice] # true or false of every elements selected in the dataframe 
#the value in the dataframe of selected company 

ppl = st.selectbox("Select a Category", new_data['cat'].unique(), index=0)
new_data= new_data[new_data['cat']== ppl]

st.write(new_data.head()) #WHYYY
st.write(f"Sum of sales {choice}:") #WHY AGAIN?????


sperweek = new_data.groupby("week")["price"].sum() #sum per week 
st.write(sperweek)

st.write(new_data["price"].sum())
st.line_chart(sperweek, y="price")

#con=sqlite.connect("Fake_sales_data.db")
#data=pd.read_