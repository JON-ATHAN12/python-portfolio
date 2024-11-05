import streamlit as st
from sent_mail import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
subject: New email from {user_email}

from: {user_email}
{raw_message}
"""

    button = st.form_submit_button("submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")