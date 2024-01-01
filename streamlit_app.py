import streamlit;
import pandas;
import requests;
import snowflake.connector;

streamlit.header('❄️ 🎅 🎅 Merry Xmas 🎅 🎅 ❄️')

streamlit.title('My First Test Page')
streamlit.header('My Header#1')
streamlit.text('✔️ My Text - 1')
streamlit.text('✔️ My Text - 2')
streamlit.text('✔️ My Text - 3')
streamlit.text('✔️ My Text - 4')

streamlit.header('🍍 🥭 🍎 🍏 🍐 🍑 🍒 🍓 My Fruit List #2 🍇 🍈 🍉 🍊 🍋 🍌 ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("🍒 🍓 Fruityvice Fruit Advice! 🍇 🍈")

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruitvice_normalized)

streamlit.header('❄️ Connecting to Snowflake ❄️')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
