import streamlit as st
import pandas as pd

# Initialize or load data
if "participants" not in st.session_state:
    st.session_state["participants"] = pd.DataFrame(columns=["Name", "Paid", "Month"])
    st.session_state["month"] = 1

# Add participants
def add_participant(name):
    st.session_state["participants"] = pd.concat(
        [st.session_state["participants"], pd.DataFrame([[name, False, st.session_state["month"]]], columns=["Name", "Paid", "Month"])],
        ignore_index=True
    )

# Update payment status
def update_payment_status():
    month = st.session_state["month"]
    st.session_state["participants"].loc[st.session_state["participants"]['Month'] == month, 'Paid'] = True

# Rotate to the next month
def next_month():
    st.session_state["month"] += 1
    st.session_state["participants"]["Paid"] = False
    st.session_state["participants"]["Month"] = st.session_state["month"]

# Main app
st.title("Quraa Management App")

# Add Participant Section
with st.expander("Add Participant"):
    name = st.text_input("Enter Participant Name")
    if st.button("Add Participant") and name:
        add_participant(name)
        st.success(f"Added {name}")

# Set Contribution Amount
st.sidebar.header("Set Contribution")
contribution_amount = st.sidebar.number_input("Contribution Amount ($)", min_value=0, value=300)

# Display Participants List and Contributions
st.subheader("Participants List")
if len(st.session_state["participants"]) > 0:
    st.write(st.session_state["participants"])
else:
    st.write("No participants added yet.")

# Current Month and Payout Information
st.sidebar.subheader(f"Month: {st.session_state['month']}")
st.sidebar.write(f"Total Contribution: ${len(st.session_state['participants']) * contribution_amount}")

# Payout Process
if st.button("Process Payment for the Month"):
    update_payment_status()
    st.success(f"Processed payments for month {st.session_state['month']}")

# Show who gets the payout this month
st.subheader(f"Participant for the payout in Month {st.session_state['month']}")
payout_person = st.session_state["participants"].iloc[st.session_state["month"] % len(st.session_state["participants"])]["Name"]
st.write(f"This month, {payout_person} will receive the pooled amount of ${len(st.session_state['participants']) * contribution_amount}")

# Proceed to the next month
if st.button("Next Month"):
    next_month()
    st.success(f"Moved to Month {st.session_state['month']}")

