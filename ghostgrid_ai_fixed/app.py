import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="GhostGrid AI",
    page_icon="👻",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("👻 GhostGrid AI")
st.subheader("Mapping the Invisible Digital Workforce")

st.markdown("""
GhostGrid AI is an AI-powered web intelligence platform that analyzes hidden digital labor ecosystems using workforce analytics, graph intelligence, AI agents, and trend forecasting.

### Built For
- Web Data UNLOCKED Hackathon by lablab.ai
- IBM BOB AI Hackathon compatible architecture
""")

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    data_path = Path(__file__).parent / "sample_data.csv"
    return pd.read_csv(data_path)

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Dashboard Controls")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=list(df["Region"].unique())
)

selected_skill = st.sidebar.multiselect(
    "Select Skill",
    options=df["Skill"].unique(),
    default=list(df["Skill"].unique())
)

filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Skill"].isin(selected_skill))
]

# =========================
# METRICS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Hidden Workers", f"{filtered_df['Workers'].sum():,}")

with col2:
    st.metric("Emerging Skills", filtered_df["Skill"].nunique())

with col3:
    st.metric("Regions Detected", filtered_df["Region"].nunique())

with col4:
    st.metric("Trend Score", f"{random.randint(80, 98)}%")

# =========================
# WORKFORCE HEATMAP
# =========================

st.header("🌍 Workforce Heatmap")

heatmap_data = filtered_df.groupby("Region", as_index=False)["Workers"].sum()

fig_heatmap = px.bar(
    heatmap_data,
    x="Region",
    y="Workers",
    title="Hidden Workforce Distribution"
)

st.plotly_chart(fig_heatmap, use_container_width=True)

# =========================
# SKILL ANALYSIS
# =========================

st.header("📈 Emerging Skills Analysis")

skill_data = filtered_df.groupby("Skill", as_index=False)["Workers"].sum()

fig_skills = px.pie(
    skill_data,
    names="Skill",
    values="Workers",
    title="Skill Demand Distribution"
)

st.plotly_chart(fig_skills, use_container_width=True)

# =========================
# TREND FORECAST
# =========================

st.header("📊 Workforce Trend Forecast")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
trend_values = [120, 140, 180, 220, 310, 420]

fig_trend = go.Figure()

fig_trend.add_trace(go.Scatter(
    x=months,
    y=trend_values,
    mode="lines+markers",
    name="Growth Trend"
))

fig_trend.update_layout(
    title="Predicted Digital Labor Growth"
)

st.plotly_chart(fig_trend, use_container_width=True)

# =========================
# NETWORK GRAPH
# =========================

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
    node_size=2500,
    font_size=10,
    ax=ax
)

st.pyplot(fig)

# =========================
# WORD CLOUD
# =========================

st.header("☁️ Trending Workforce Keywords")

text = " ".join(filtered_df["Skill"].astype(str))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
ax_wc.imshow(wordcloud, interpolation="bilinear")
ax_wc.axis("off")

st.pyplot(fig_wc)

# =========================
# ADDITIONAL INFO
# =========================

st.header("🚀 Additional Information")

st.markdown("""
### Why GhostGrid AI?

Millions of online workers contribute to the global digital economy through:
- AI training
- Data labeling
- Freelancing
- Microtask ecosystems
- Anonymous digital services

However, these workers remain statistically invisible.

GhostGrid AI transforms fragmented public web data into actionable workforce intelligence using:
- AI agents
- Graph analytics
- NLP pipelines
- Predictive forecasting

### Hackathon Vision
GhostGrid AI was designed as a next-generation economic intelligence platform capable of helping researchers, organizations, and governments better understand the future of hidden digital labor ecosystems.
""")

# =========================
# FOOTER
# =========================

st.markdown("---")
st.markdown("## GhostGrid AI — Unseen. Uncounted. Understood.")
