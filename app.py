import streamlit as st

# st.title("Hello World")
# st.write("simple app using streamlit")
# st.success("Success")
# st.error("Error")
# st.warning("Warning")
# st.info("Info")

# pip install pillow
# from PIL import Image
# img = Image.open("streamlit.png")
# st.image(img, width=400)


# btn = st.button("Increment")

# if "count" not in st.session_state:
#     st.session_state.count = 0

# if btn:
#     st.session_state.count += 1
#     st.write(f"button Clicked {st.session_state.count} times")



chat_input = st.chat_input("Enter your prompt")

if chat_input:
    # st.write(chat_input)
    st.chat_message("user").write(chat_input)
    st.chat_message("assistant").write("Hello how can I help you today?")

# def check_admin( func ):
#     def wrapper():
#         print("Checking if user is admin") 
#         func()
#     return wrapper
    

# @check_admin
# def greet():
#     print("Hello World")

# greet()