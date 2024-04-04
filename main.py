import streamlit as st

st.title("Hi I am streamlit web app")
st.subheader("Hi I am your subheader")
st.header("I am Header")
st.text("Hi I am text function and programmers uses me in place of paragraph text")
st.markdown("# Hello World")
st.markdown("*This is italics*")
st.markdown("**this is bold**")
st.markdown("---") #this is a line
st.markdown("[Google](https://www.google.com)") #this creates a hyperlink
st.caption("Hi I am Caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") #mathematical expression
json={"a":"1,2,3","b":"4,5,6"} #defined variable
st.json(json)
code="""
print(Hello World)
def funct():
    return 0;"""
st.code(code, language="python") #creating python block code
st.write("## H2")