import streamlit;
import pandas;
import requests;
import snowflake.connector;
from urllib.error import URLError

streamlit.header('❄️ 🎅 🎅 Merry Xmas 🎅 🎅 ❄️')

streamlit.title('My First Test Page')
streamlit.header('My Header#1')
streamlit.text('✔️ My Text - 1')
streamlit.text('✔️ My Text - 2')
streamlit.text('✔️ My Text - 3')
streamlit.text('✔️ My Text - 4')

streamlit.header('🍍 🥭 🍎  My Fruit List #2 🍇 🍈 🍉  ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#################################################################################
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
   streamlit.error()

#streamlit.stop()


#streamlit.header("### Fruityvice ###")
#streamlit.header("🍒 🍓 Fruityvice Fruit Advice! - Errorhandler 🍇 🍈")
#try:
#  fruit_choice = streamlit.text_input('What fruit would you like information about?')
#  if not fruit_choice:
#    streamlit.error("Please select a fruit to get information. ")   
#  else:
#    fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#    fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
#    streamlit.dataframe(fruitvice_normalized)
# except URLError as e:
#    streamlit.error()

#################################################################################
#streamlit.header("### Snowflake ###")
#streamlit.header('❄️ Connecting to Snowflake ❄️')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
## my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("select * from fruit_load_list")
## my_data_row = my_cur.fetchone()
#my_data_rows = my_cur.fetchall()
s#treamlit.text("The fruit load list contains:")
##streamlit.text(my_data_row)
#streamlit.dataframe(my_data_rows)

#fruit_add = streamlit.text_input('What fruit would you like to add ? ','Jackfruit')
#streamlit.write('Thanks for adding :', fruit_add)

#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")

streamlit.header("### Snowflake ###")

streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# add a button to load the fruit
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
