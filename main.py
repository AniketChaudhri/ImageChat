import streamlit as st

st.title('Ask a question to an image')
st.header('Upload an image')
file = st.file_uploader('Upload an image', type=['jpg', 'png', 'jpeg'])
if file is not None:
    st.image(file, use_column_width=True)
    user_question = st.text_input('Ask a question to the image')
    if user_question:
        st.write('You asked: ', user_question)
        st.write('Answer: ', 'This is a placeholder answer')