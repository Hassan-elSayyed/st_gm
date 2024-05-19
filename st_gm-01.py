import streamlit as st 
import plotly.offline as py
# py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
from plotly.figure_factory import create_table

subject = 'gapminder'
# df = px.data.gapminder()
# table = create_table(df.head(10))
# py.iplot(table)
# print(table)

# @st.cache_data
# def lifespan_gdp():
#     labels = dict(pop='Population', gdpPercap='DGP per Capita', lifeExp='Life Expectancy')
#     px.scatter(gm_df, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, hover_name='country', animation_frame='year', animation_group='country', log_x=True, range_x=[100, 100000], range_y=[25, 90], labels=labels)
# gm = lifespan_gdp()
# st.write(gm)
    
st.header('Lifespan correlation with Gross Domestic Product')
st.markdown('GDP per capita increases the life expectancy at birth through increasing economic growth and development in a country and thus leads to the prolongation of longevity (Loichinger & Weber, 2019, p.)')
st.markdown('###### Loichinger, E., & Weber, D. (2019). Trends in healthy life expectancy between 2000 and 2017: An analysis based on 38 countries. Genus, 75(2). https://doi.org/10.1186/s41118-019-0071-0')
st.markdown('\n\n')
st.markdown("##### `Hover or click any where there is something!`")

gm_df = px.data.gapminder()
@st.cache_data
def lifespan():
    labels = dict(pop='Population', gdpPercap='DGP per Capita', lifeExp='Life Expectancy')
    fig = px.scatter(gm_df, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, hover_name='country', animation_frame='year', animation_group='country', log_x=True, range_x=[250, 100000], range_y=[25, 90], labels=labels, width=700, height=600)
    # fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    return fig
bubble_anim = lifespan()
st.write(bubble_anim)