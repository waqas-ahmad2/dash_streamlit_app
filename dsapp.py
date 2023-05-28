import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

#data
df = pd.read_csv('india_final.csv')

state_names = df.State.unique().tolist()
state_names.insert(0,'All') #adding All in the beginning

primary = sorted(df.columns[5:])
secondary = primary

#streamlit components

#sidebar
st.sidebar.title('Indian Census Data App')
state = st.sidebar.selectbox('Select State',options=state_names)
primary = st.sidebar.selectbox('Select Primary Parameter',options=primary)
secondary = st.sidebar.selectbox('Select Secondary Parameter',options=secondary)
btn_plot = st.sidebar.button('Plot')

#graphs
if btn_plot:
    if state == 'All':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,
                            color=secondary,zoom=3, mapbox_style='carto-positron',
                            hover_name='District',width=1200, height=700)
        st.plotly_chart(fig,use_container_width=True,)
    else:
        mask=df[df["State"]==state]
        fig = px.scatter_mapbox(mask,lat='Latitude',lon='Longitude',size=mask[primary],
                            color=mask[secondary], hover_name='District', zoom=3,
                            mapbox_style='carto-positron', width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True)

