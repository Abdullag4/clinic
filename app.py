import streamlit as st
import pandas as pd

# Sample data for the clinic
data = {
    "Client Name": ["Alice Johnson", "Bob Smith", "Charlie Brown"],
    "Age": [34, 45, 29],
    "Visit Date": ["2024-11-01", "2024-11-15", "2024-11-20"],
    "Service": ["Dental Checkup", "General Consultation", "Eye Test"],
    "Fees Paid": [50, 30, 40]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# App Title
st.title("Clinic Data Dashboard")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Add Client Data"])

# Dashboard
if page == "Dashboard":
    st.header("Client Overview")
    st.dataframe(df)

    st.subheader("Summary")
    total_clients = len(df)
    total_fees = df["Fees Paid"].sum()
    st.write(f"**Total Clients:** {total_clients}")
    st.write(f"**Total Fees Collected:** ${total_fees}")

# Add Client Data
if page == "Add Client Data":
    st.header("Add New Client Data")
    with st.form("client_form"):
        name = st.text_input("Client Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        visit_date = st.date_input("Visit Date")
        service = st.text_input("Service")
        fees_paid = st.number_input("Fees Paid", min_value=0, step=1)
        submitted = st.form_submit_button("Submit")

    if submitted:
        # Add new data to DataFrame (in practice, this would be saved to a database)
        new_data = {
            "Client Name": name,
            "Age": age,
            "Visit Date": visit_date.strftime("%Y-%m-%d"),
            "Service": service,
            "Fees Paid": fees_paid
        }
        df = df.append(new_data, ignore_index=True)
        st.success("New client data added!")
        st.write("Updated Data:")
        st.dataframe(df)
