import contextlib
from reader import Reader
import streamlit as st

from utils import savefile
st.title("Contextual ChatBot")

def runBot():
    readerObj = Reader()

    uploader=st.file_uploader("Enter your Document",type=["txt","pdf", "docx"])
    with contextlib.suppress(Exception):
        filename=savefile(path="Data/",uploaded_file=uploader)
        text = readerObj.read_document(filename)
        st.header("Text:")
        st.write(text)

        st.header("Chunks")
        chunk_size = st.slider("Use this", min_value=0, max_value=len(text), value=644)
        question = st.text_input("Ask a question:")

    if submit := st.button("Ask"):
        chunks = readerObj.create_chunks(text, chunk_size)
        st.write("The number of paragraphs created:",len(chunks))
        st.write(question)

runBot()