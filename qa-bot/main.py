import streamlit as st
import os
import requests
import logging

logger = logging.getLogger(__name__)

def save_uploaded_file(uploaded_file):
    with open(os.path.join("data", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File saved successfully!")
    return uploaded_file.name

def download_file_from_url(url, filename):
    try:
        import requests
    except ImportError:
        st.error("The 'requests' module is required for downloading files.")
        logger.error("The 'requests' module is required for downloading files.")
        return

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join("data", filename), "wb") as f:
                f.write(response.content)
            st.success("File downloaded and saved successfully!")
        else:
            st.error(f"Failed to download file from {url}")
            logger.error(f"Failed to download file from {url}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        logger.error(f"An error occurred: {str(e)}")

def chat(query):
    # Here you would put your logic to generate a response based on the query
    # For now, let's just echo the query as the response
    return query

def main():
    st.title("Welcome to Your App")
    st.write("This app allows you to explore and interact with data.")

    if st.button("Explore Now"):
        st.session_state.page = "explore"

    if st.session_state.get("page") == "explore":
        explore()

def explore():
    st.title("Explore Page")
    st.write("On this page, you can add data to chat or chat with existing knowledge.")

    if st.button("Add Data to Chat"):
        st.session_state.page = "add_data"

    if st.session_state.get("page") == "add_data":
        add_data_to_chat()

    if st.button("Chat with Existing Knowledge"):
        st.session_state.page = "chat_default"

    if st.session_state.get("page") == "chat_default":
        chat_with_knowledge()

    if st.session_state.get("chatting"):
        query = st.text_input("Ask a question:")
        if st.button("Chat"):
            response = chat(query)
            st.text_area("Response:", value=response, height=200)

def add_data_to_chat():
    st.title("Add Data to Chat")
    st.title("File Uploader and Downloader")

    option = st.radio("Choose an option", ("Upload a file", "Download from URL"), index = None)

    if option == "Upload a file":
        st.session_state.page = "file_upload"
        uploaded_file = st.file_uploader("Choose a file", type=['csv', 'txt'])
        if uploaded_file is not None:
            filename = save_uploaded_file(uploaded_file)
            st.write("You have uploaded:", filename)
            if st.button("Start Chatting"):
                st.session_state.page = "chat"
    elif option == "Download from URL":
        st.session_state.page = "file_download"
        url = st.text_input("Enter the URL:")
        if st.button("Download"):
            filename = url.split("/")[-1]
            download_file_from_url(url, filename)
            st.success("File downloaded successfully!")
            st.write("You have downloaded:", filename)
            if st.button("Start Chatting"):
                st.session_state.page = "chat"
                
def chat_with_knowledge():
    st.title("Chat with Existing Knowledge")
    query = st.text_input("Ask a question:")
    if st.button("Chat"):
        response = chat(query)
        st.text_area("Response:", value=response, height=200)

if __name__ == "__main__":
    main()
