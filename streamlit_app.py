 
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

# new 
streamlit.header('My fruityvise advice!')
fruit_choice =streamlit.text_input('what fruit whould you like to have ?','kiwi')
streamlit.write('The user entered ' ,fruit_choice)
import requests
fruityvice_response =requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
df = pandas.read_json(fruityvice_response.text)
streamlit.dataframe(df)
import snowflake.connector



