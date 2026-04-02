import streamlit as st
import pandas as pd
 
# Title & Subheader 
st.title("📊 Sales Summary Dashboard")
st.subheader("Simple interactive app to explore sales by category")

# Create Hardcoded DataFrame
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [1200, 800, 450, 150, 300]
}

df = pd.DataFrame(data)
 
# Sidebar Filter (Task 2) 
st.sidebar.header("Filter Options")

category = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique()
)
 
# Filter Data 
filtered_df = df[df["Category"] == category]
 
# Display Filtered Data 
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)
 
# Line Chart 
st.write("### Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])