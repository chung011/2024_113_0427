import streamlit as st

st.bar_chart({"data":[1, 5, 2, 6, 2, 1]})
're '
with st.expander('see explanation'):
    st.markdown('''
                ###Chart above
                    - The chart above shows some numbers I picked for you.
                    - I rolled actural dice for these, so they're ** guaranteed**
                    
    > to be random.            
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
    