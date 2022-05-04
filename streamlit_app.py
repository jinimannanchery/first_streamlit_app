 
import streamlit
import pandas


streamlit.title("My Parents new Healthy Diner")
streamlit.header ('Breakfast Menu')
streamlit.text ('Dosa')
streamlit.text ('Appam')
streamlit.text ('Kappa Fish Curry')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some  Fruits :" ,list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
import requests
import snowflake.connector

ctx = snowflake.connector.connect(
    user='jinikadankavil',
    password='zxcv@1234',
    account='ye90206.ca-central-1.aws'
    )
