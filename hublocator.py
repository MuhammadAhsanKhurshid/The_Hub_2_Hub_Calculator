import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("dummy_node_distances.csv")

st.set_page_config(page_title="Hub Locator", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff5733;'>📍 Hub Locator</h1>", unsafe_allow_html=True)
st.write("Select two nodes to see distance and travel time.")

nodes = sorted(set(df['Node1']).union(set(df['Node2'])))

col1, col2 = st.columns(2)
with col1:
    node1 = st.selectbox("Select Origin Node", nodes)
with col2:
    node2 = st.selectbox("Select Destination Node", nodes)

if st.button("Calculate Distance"):
    if node1 == node2:
        st.warning("Please select two different nodes.")
    else:
        row = df[((df['Node1']==node1) & (df['Node2']==node2)) | ((df['Node1']==node2) & (df['Node2']==node1))]
        if not row.empty:
            distance = row['Distance_km'].values[0]
            time = row['Time_min'].values[0]
            st.success(f"🚚 Distance between **{node1} → {node2}**: **{distance} km**  
⏱ Estimated Time: **{time} min**")
        else:
            st.error("No data found for selected nodes.")
