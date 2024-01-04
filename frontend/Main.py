import streamlit as st

st.set_page_config(
    page_title="Flipando - ORT",
)

exercise = {"instructions": "Read the text below and think of the word which best fits each gap. Use only one word in each gap. There is an example at the beginning (0).", "title": "Motorbike stunt rider", "text": ["I work (0)______ a motorbike stunt rider \u2013 that is, I do tricks on my motorbike at shows.", "The Le Mans race track in France was (9)______ . I first saw some guys doing motorbike stunts.", "I\u2019d never seen anyone riding a motorbike using just the back wheel before and I was (10)______ impressed I went straight home and taught (11)______ to do the same.", "It wasn\u2019t very long before I began to earn my living at shows performing my own motorbike stunts.", "I have a degree (12)______ mechanical engineering; this helps me to look at the physics (13)______ lies behind each stunt.", "In addition to being responsible for design changes to the motorbike, I have to work (14)______ every stunt I do.", "People often think that my work is very dangerous, but, apart (15)______ some minor mechanical problem happening occasionally during a stunt, nothing ever goes wrong.", "I never feel in (16)______ kind of danger because I\u2019m very experienced."], "example": {"number": "0", "answer": "AS"}, "questions": {"1": "", "2": "", "3": "", "4": "", "5": "", "14": "", "15": "", "16": ""}}

st.markdown("""
    <style>
    h1, h2, h3, h4, h5, h6, p {
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

st.write("# Are you ready to practice your English?")

st.write("Select one of the options on the sidebar to start.")