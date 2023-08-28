import streamlit as st
import sqlite3
name = st.text_input("username", "")
password = st.text_input("password", "")
conn = sqlite3.connect('pyps.db')
cur = conn.cursor()
user = (name, password)
cur.execute("""CREATE TABLE IF NOT EXISTS pyps(
           name TEXT PRIMARY KEY,
           password TEXT);
        """)
st.write(user)
cur.execute("SELECT * FROM pyps;")
st.write(cur.fetchall())
if st.button("sign up"):
    try:
        cur.execute("INSERT INTO pyps VALUES(?, ?);", user)
        conn.commit()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pyps;")
        st.write(cur.fetchall())
        st.success('Hi')
    except:
        st.write('try again')
elif st.button('sign in'):
        cur.execute("SELECT * FROM pyps;")
        if user in cur.fetchall():
            st.success('Hi')
        else:
            st.write("try again")
