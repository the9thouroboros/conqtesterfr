import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Conquest",
    layout="wide"
)

# Sidebar with larger logo
with st.sidebar:
    # Logo at the top of the sidebar - now 2x bigger (width=400)
    st.image("CONQUESTLOGO.png", width=400)
    
    # Add some spacing
    st.markdown("##")
    
    # Simple navigation menu
    st.markdown("### Navigation")
    st.button("Home")
    st.button("About")
    st.button("Contact")

# Main content area
st.title("Welcome to Conquest")
st.write("This is a demonstration of a Streamlit site with the logo only in the sidebar.")
