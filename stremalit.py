import streamlit as st
import seaborn as sns
import altair as alt
import numpy as np


st.title('Penguins in streamlit')

penguins = sns.load_dataset('penguins')

st.line_chart(penguins['body_mass_g'])


