import streamlit
import pandas

streamlit.header('❄️ 🎅 🎅 Merry Xmas 🎅 🎅 ❄️')

streamlit.title('My First Test Page')
streamlit.header('My Header#1')
streamlit.text('✔️ My Text - 1')
streamlit.text('✔️ My Text - 2')
streamlit.text('✔️ My Text - 3')
streamlit.text('✔️ My Text - 4')

streamlit.header('🍍 🥭 🍎 🍏 🍐 🍑 🍒 🍓 My Fruit List #2 🍇 🍈 🍉 🍊 🍋 🍌 ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pisk some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
