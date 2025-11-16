import streamlit as st
import pandas as pd
import plotly.express as px


df_vehicles = pd.read_csv("/vehicles_us.csv")
df_vehicles.info()
