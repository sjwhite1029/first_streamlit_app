import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruity_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruity_list = my_fruity_list.set_index('Fruit')

# Let's put al pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruity_list.index), ['Avocado', 'Strawberries'])

# display the talbe on the page
streamlit.dataframe(my_fruity_list)
