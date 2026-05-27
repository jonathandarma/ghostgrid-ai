import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="GhostGrid AI", layout="wide")

st.title("👻 GhostGrid AI")
st.subheader("Mapping the Invisible Digital Workforce")

st.markdown("""
GhostGrid AI is an AI-powered web intelligence platform that analyzes hidden digital labor ecosystems using workforce analytics, graph intelligence, and trend forecasting.
""")

@st.cache_data
def load_data():
    return pd.read_csv("sample_data.csv")

df = load_data()

st.sidebar.title("Dashboard Controls")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

selected_skill = st.sidebar.multiselect(
    "Select Skill",
    options=df["Skill"].unique(),
    default=df["Skill"].unique()
)

filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Skill"].isin(selected_skill))
]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Hidden Workers", f"{len(filtered_df) * 12:,}")

with col2:
    st.metric("Emerging Skills", filtered_df["Skill"].nunique())

with col3:
    st.metric("Regions Detected", filtered_df["Region"].nunique())

with col4:
    st.metric("Trend Score", f"{random.randint(80, 98)}%")

st.header("🌍 Workforce Heatmap")

heatmap_data = filtered_df.groupby("Region")["Workers"].sum().reset_index()

fig_heatmap = px.bar(
    heatmap_data,
    x="Region",
    y="Workers",
    title="Hidden Workforce Distribution",
)

st.plotly_chart(fig_heatmap, use_container_width=True)

st.header("📈 Emerging Skills Analysis")

skill_data = filtered_df.groupby("Skill")["Workers"].sum().reset_index()

fig_skills = px.pie(
    skill_data,
    names="Skill",
    values="Workers",
    title="Skill Demand Distribution"
)

st.plotly_chart(fig_skills, use_container_width=True)

st.header("📊 Workforce Trend Forecast")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
trend_values = [120, 140, 160, 210, 280, 340]

fig_trend = go.Figure()

fig_trend.add_trace(go.Scatter(
    x=months,
    y=trend_values,
    mode='lines+markers',
    name='Growth Trend'
))

fig_trend.update_layout(title="Predicted Digital Labor Growth")

st.plotly_chart(fig_trend, use_container_width=True)

st.header("🕸 Hidden Labor Network")

G = nx.Graph()

skills = filtered_df["Skill"].unique()
regions = filtered_df["Region"].unique()

for skill in skills:
    for region in regions:
        G.add_edge(skill, region)

pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(10, 6))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=10,
    ax=ax
)

st.pyplot(fig)

st.header("☁️ Trending Workforce Keywords")

text = " ".join(filtered_df["Skill"])

wordcloud = WordCloud(width=800, height=400).generate(text)

fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis("off")

st.pyplot(fig_wc)

st.markdown("---")
st.markdown("### GhostGrid AI — Unseen. Uncounted. Understood.")
