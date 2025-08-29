import streamlit as st
import pandas as pd

# App title
st.set_page_config(page_title="Hub-to-Hub Distance Calculator", layout="centered")

st.title("📍 Hub-to-Hub Distance Calculator")
st.markdown("Easily check road distances and travel time between logistics hubs.")

# Load fixed dataset
df = pd.read_csv("dummy_node_distances.csv")

# Collect all unique hub names
nodes = sorted(set(df["Node1"]).union(set(df["Node2"])))

# Dropdowns with hub names (like CTN, BDD, etc.)
node1 = st.selectbox("From (Origin Hub)", nodes)
node2 = st.selectbox("To (Destination Hub)", nodes)

if st.button("🔍 Calculate Distance"):
    row = df[((df["Node1"] == node1) & (df["Node2"] == node2)) |
             ((df["Node1"] == node2) & (df["Node2"] == node1))]

    if not row.empty:
        distance = row.iloc[0]["Distance_km"]
        time = row.iloc[0]["Time_min"]

        st.success(f"""
        **From Hub:** {node1}  
        **To Hub:** {node2}  

        🚚 **Distance**: {distance} km  
        ⏱️ **Estimated Time**: {time} minutes
        """)
    else:
        st.error("❌ No road distance found between the selected hubs.")

