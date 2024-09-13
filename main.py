import streamlit as st
import textwrap
import helper

# Initialize the Streamlit app
st.set_page_config(layout="wide")

def main():
    # App title and description
    st.title("Youtube Search App")
    st.markdown("Enter a YouTube URL and a query to get a summarized response.")
    # Sidebar for inputs
    with st.sidebar:
        st.header("Search Parameters")
        url = st.text_input("URL", placeholder="Enter YouTube URL here...")
        query = st.text_input("Query", placeholder="Enter your search query...")
        submit_button = st.button("Submit")

    # Search functionality
    if submit_button:
        db_s = {}
        if url not in db_s:
            try:
                db = helper.youtube_url_to_db(url)
                db_s[url] = db
            except Exception as e:
                st.error(f"Failed to process URL: {e}")
                return
        else:
            db = db_s[url]
            st.info("Using cached data for this URL.")

        try:
            summary = helper.get_resp_query(db, query, k=3)
            if summary:
                with st.expander("Search Summary", expanded=True):
                    st.markdown(f"**Summary:**\n{textwrap.fill(summary, width=85)}")
            else:
                st.warning("No results found for the given query.")
        except Exception as e:
            st.error(f"Error during search: {e}")
    st.markdown("by raja ")

if __name__ == '__main__':
    main()