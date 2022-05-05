 
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response =requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvise_normalized=pandas.json_normalize(fruityvice_response.json())
    return fruityvise_normalized

streamlit.header('My fruityvise advice!')
try:
  fruit_choice =streamlit.text_input('what fruit whould you like to have ?')
  if not  fruit_choice:
       streamlit.error("Please select a fruit to get information.")
  else:
       back_from_function=get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
   

streamlit.header("The Fruit load list contains:")
def get_fruitload_list():
   with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from  FRUIT_LOAD_LIST")
       return  my_cur.fetchall()
#Add button  to load the fruit
if streamlit.button('Get fruitload list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruitload_list()
    streamlit.dataframe(my_data_row)
#streamlit.stop()
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('from streamlit')")
       return("Thanks  for adding '+new_fruit")
   
add_my_fruit =streamlit.text_input('what fruit whould you like to add ?')
if streamlit.button('Add fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function=insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)


