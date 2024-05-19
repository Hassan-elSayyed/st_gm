import streamlit as st 
import pandas as pd
import numpy as np

import plotly.express as px

subject = 'gapminder'
    
st.header('Lifespan correlation with Gross Domestic Product')
st.markdown('GDP per capita increases the life expectancy at birth through increasing economic growth and development in a country and thus leads to the prolongation of longevity (Loichinger & Weber, 2019, p.)')
st.markdown('###### Loichinger, E., & Weber, D. (2019). Trends in healthy life expectancy between 2000 and 2017: An analysis based on 38 countries. Genus, 75(2). https://doi.org/10.1186/s41118-019-0071-0')
st.markdown('\n\n')
st.markdown("##### `Hover or click any where there is something!`")

gm_df = px.data.gapminder()
@st.cache_data
def lifespan():
    labels = dict(pop='Population', gdpPercap='GDP per capita', lifeExp='Life Expectancy')
    fig = px.scatter(gm_df, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, hover_name='country', animation_frame='year', animation_group='country', log_x=True, range_x=[250, 100000], range_y=[25, 90], labels=labels, width=700, height=600)
    # fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    return fig
bubble_anim = lifespan()
st.write(bubble_anim)

df = px.data.gapminder()
df.rename(columns={'country':'Country', 'continent':'Continent', 'year':'Year', 'lifeExp':'Life Expectancy', 'pop':'Population', 'gdpPercap':'GDP Per Capita'}, inplace=True)
df.set_index('Country', inplace=True)
if st.checkbox('Display Source Data', True):
    # st.subheader('Source Data')
    st.write(df)
