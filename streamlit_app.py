 
import streamlit
import pandas
import requests
import snowflake.connector
import urllib.error
import URLError

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

fruityvice_response =requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
df = pandas.read_json(fruityvice_response.text)
streamlit.dataframe(df)
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from  FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_row)
add_my_fruit =streamlit.text_input('what fruit whould you like to add ?','jackfruit')
streamlit.write('Thanks for adding ' ,add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

