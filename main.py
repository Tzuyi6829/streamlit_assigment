#streamlit: an application (web server) that is able to respond to web browswer (to display the results)
#replit: website where we work on 
#github: library where the codes are stored
#pandas : excel in python
#numpy: engine of pandas 

#Instructions:
#go in Shell (on the right)
#write "pip install --upgrade streamlit"
#write "pip install plotly-express"
#launch with "streamlit run main.py"


#st.write(new_data["price"].sum())
#st.line_chart(sperweek, y="price")

#con=sqlite.connect("Fake_sales_data.db")
#data=pd.read_



# streamlit run main.py ---- to see website

# Imports required ---
import streamlit as st #nickname 
import sqlite3 as sqlite #sqlite: database 
import pandas as pd #operation 
import plotly.express as px

@st.cache_data #function enables the code to avoid running from the top to the bottom everytime
def get_data():
  con = sqlite.connect("Fake_sales_data.db") #connect to the databse file
  data = pd.read_sql_query("SELECT * from SalesA", con) #fetching the data from SalesA table (in sql) + connect to the table SalesA
  return data
data = get_data() #call the function to get the value, value in "data"

st.title('Sales Dashboard') #create the title in website 
st.write(f"We have {len(data)} datapoints") #st.write: to write a caption below 

choice = st.selectbox("Select a Company", data["company"].unique(),index=0)
#unique:equals to "distinct" in sql 
#choice:variable(the one selected)
#index(int):index of the preselected option on first render
new_data = data[data["company"] == choice] 
#true or false of every elements selected in the dataframe 
#the value in the dataframe of selected company 
st.write(new_data.groupby(["cat"])["price"].unique())

ppl = st.selectbox("Select a Category", new_data['cat'].unique(), index=0)
new_data= new_data[new_data['cat']== ppl] #NOT SURE 

#st.write(new_data.head()) ---?

choicedemo = st.multiselect("Select demographic", new_data["cat"].unique())
www = new_data["cat"].isin(choicedemo)
new_dataa = new_data[www]

choiceprice = st.multiselect("Select price", new_dataa["price"].unique())
wwa = new_dataa["price"].isin(choiceprice)
new_data_price = new_dataa[wwa]

st.write(new_data_price.head())

#st.write(new_data.head())
#st.write(f"Sum of Sales {choice}:")
#st.write(new_data["price"].sum())

st.write(f"Volume of Sales {choice}:")
#embed variable with "f"
volum = new_data["price"].count()
st.write(volum)
# print the data / week
#-----st.write(f"Volume of Sales per week {choice}:")
sumperweek = new_data.groupby(["week"])["price"].count()

#st.write(sperweek)
sumperweek = new_data.groupby(["week"])["price"].count().reset_index()

#revenue
st.write(f"Revenue of {choice}:")
#embed variable with "f" (variable=choice)
revenue = new_data["price"].sum()
st.write(revenue)
sumperweekk = new_data.groupby(["week"])["price"].sum()

#st.write(sumperweek)
sumperweekk = new_data.groupby(["week"])["price"].sum().reset_index()

# plot volume & revenue through time
tab1, tab2 = st.tabs(["Volume", "Revenue"])
with tab1:
  figvol = px.line(sumperweek, x="week", y="price", title='Volume through time') 
  #line():draw a line in the image 
  #px--- create entire figure 
  st.plotly_chart(figvol)

with tab2:
  figrev = px.line(sumperweekk, x="week", y="price", title='Revenue through time')
  st.plotly_chart(figrev)