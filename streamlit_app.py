import streamlit;
import pandas;
import requests;

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

fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruitvice_normalized)

