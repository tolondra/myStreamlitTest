import streamlit as st



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from functions import *
from helper_Functions import *


if __name__ == "__main__":
    # """
    # Main function to run the Streamlit app. It sets up the sidebar, imports data, creates sliders,
    # filters the data, and provides options for visualizing and downloading the data.
    # """
    # Set the title for the sidebar
    st.sidebar.title("Hello Daniel! We could deploy the WUI here")
    st.sidebar.write("")

