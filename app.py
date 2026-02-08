import streamlit as st
import random

# Set page configuration for a romantic feel
st.set_page_config(page_title="A Special Message for You", page_icon="❤️")

# Custom CSS for the "Floating/Dodging" No button and romantic styling
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
    }
    /* The trick for the No button */
    #no-button-container {
        display: inline-block;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# App Content
st.title("💖 Hey Beautiful...")
st.header("I've missed you so much!")

st.write("""
Now that I'm finally coming back to you tomorrow . i have request for you , can u please take a holiday from all the workload of office and be there with me the whole day , watching shwos , cooking together , desigining room , deep convos and much more 
 I want us to forget the world, forget the office, and just be with me .
""")

st.subheader("so will be my valentine ? ")

# Create two columns for the buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 😍"):
        st.balloons()
        st.snow() # Looks like falling petals/confetti in this context
        st.success("Yay! I can't wait to see you tomorrow! Prepare for the best day ever. ❤️")
        st.confetti() # If you have the streamlit-confetti transition

with col2:
    # This is the "No" button logic using a bit of Streamlit's session state
    if "no_count" not in st.session_state:
        st.session_state.no_count = 0

    # We use a trick: every time the "No" button is targeted or the page reruns, 
    # we can change its position or label to make it "unclickable"
    no_labels = ["No", "Are you sure?", "Really?", "Think again!", "Pfft, try again!", "Not an option! 😉"]
    
    if st.button(no_labels[st.session_state.no_count % len(no_labels)]):
        st.session_state.no_count += 1
        st.warning("Error 404: 'No' not found. Please try the other button! or if sure no then click no again 😘")


st.write("---")
st.caption(" with ❤️  prem .")
