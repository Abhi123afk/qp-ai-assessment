import os
from pathlib import Path
import streamlit as st

working_dir=os.getcwd()
def delete(directory):
    for files in os.listdir(directory):
        path = os.path.join(directory, files)
        os.remove(path)

def createtext(path,string):
    with open(path, "w") as text_file:
        text_file.write(string)

def showtext(directory):
    p1 = Path(directory)
    for j in list(p1.glob('*')):
        with open(str(j),"r",encoding='utf-8') as t:
            stringtoshow=t.read()
            st.write(stringtoshow)

def createtextextension(name):
    return name.split("/")[-1].split(".pdf")[0] + ".txt"



def savefile(path,uploaded_file):
    save_path = f"{working_dir}/{path}"
    with open(os.path.join(save_path, uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())
        filename = f"{working_dir}/{path}{str(uploaded_file.name)}"
    return filename



working_dir=os.getcwd()

def delete(directory):
    for files in os.listdir(directory):
        path = os.path.join(directory, files)
        os.remove(path)

def createtext(path,string):
    with open(path, "w") as text_file:
        text_file.write(string)

def showtext(directory):
    p1 = Path(directory)
    for j in list(p1.glob('*')):
        with open(str(j),"r",encoding='utf-8') as t:
            stringtoshow=t.read()
            st.write(stringtoshow)

def createtextextension(name):
    return name.split("/")[-1].split(".pdf")[0] + ".txt"


def savefile(path,uploaded_file):
    save_path = f"{working_dir}/{path}"
    with open(os.path.join(save_path, uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())
        filename = f"{working_dir}/{path}{str(uploaded_file.name)}"
    return filename
