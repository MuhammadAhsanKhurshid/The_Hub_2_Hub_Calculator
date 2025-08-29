import streamlit as st
import pandas as pd

# App title
st.set_page_config(page_title="Hub-to-Hub Distance Calculator", layout="centered")

st.title("📍 Hub-to-Hub Distance Calculator")
st.markdown("Easily check road distances and travel time between logistics nodes.")

# Load fixed dataset (already in repo)
df = pd.read_csv("dummy_node_distances.csv")

# Dropdowns for selecting nodes
nodes = sorted(df["Node1"].unique().tolist() + df["Node2"].unique().tolist())
node1 = st.selectbox("Select **Origin Node**", nodes)
node2 = st.selectbox("Select **Destination Node**", nodes)

if st.button("🔍 Calculate Distance"):
    # Try to find matching row in either direction
    row = df[((df["Node1"] == node1) & (df["Node2"] == node2)) |
             ((df["Node1"] == node2) & (df["Node2"] == node1))]

    if not row.empty:
        distance = row.iloc[0]["Distance_km"]
        time = row.iloc[0]["Time_min"]

        st.success(f"""
        🚚 **Distance**: {distance} km  
        ⏱️ **Estimated Time**: {time} minutes
        """)
    else:
        st.error("No distance found between the selected nodes.")


