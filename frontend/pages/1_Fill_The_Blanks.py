import streamlit as st

st.set_page_config(page_title="Fill the blanks")

st.markdown("""
    <style>
    h1, h2, h3, h4, h5, h6, p {
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

exercise_content = exercise = {
  "title": "Motorbike stunt rider",
  "text": [ #separado por parrafo
    "I work (0)______ a motorbike stunt rider \u2013 that is, I do tricks on my motorbike at shows. The Le Mans race track in France was (1)______ . I first saw some guys doing motorbike stunts. I\u2019d never seen anyone riding a motorbike using just the back wheel before and I was (2) ______ impressed I went straight home and taught (3)______ to do the same. It wasn\u2019t very long before I began to earn my living at shows performing my own motorbike stunts.",
    "I have a degree (4)______ mechanical engineering; this helps me to look at the physics (5)______ lies behind each stunt. In addition to being responsible for design changes to the motorbike, I have to work (6)______ every stunt I do. People often think that my work is very dangerous, but, apart (7)______ some minor mechanical problem happening occasionally during a stunt, nothing ever goes wrong. I never feel in (8)______ kind of danger because I\u2019m very experienced."
  ],
  "example": { "number": "0", "answer": "AS" },
  "questions": {
    1: "AMAZING",
    2: "SO",
    3: "MYSELF",
    4: "IN",
    5: "THAT",
    6: "ON",
    7: "FROM",
    8: "ANY",
  },
}

st.markdown("# Fill the blanks")

st.write(
    """Read the text below and think of the word which best fits each gap. Use only **one** word in each gap. There is an example at the beginning **(0)**."""
)

st.write(f"### {exercise_content['title']}")

st.write(f"**Example:** {exercise_content['example']['number']} - {exercise_content['example']['answer']}")

user_answers = {}

for index, text in enumerate(exercise_content['text']):
  st.write(f"{text}")

for question_num in range(1, len(exercise_content['questions']) + 1):
    user_answers[question_num] = st.text_input(f"Enter your answer for ({question_num})", key=f"question_{question_num}")

col1, col2 = st.columns([0.8, 0.2])

with col2:
    if st.button('Check Answers'):
        correct_answers = 0
        for question_num, user_answer in user_answers.items():
            if user_answer.lower() == exercise_content['questions'][question_num].lower():
                correct_answers += 1
                st.success(f"Correct for ({question_num})!")
            else:
                st.error(f"Incorrect for ({question_num}). The correct answer is {exercise_content['questions'][question_num]}.")
        st.write(f"You got {correct_answers} out of {len(exercise_content['questions'])} correct.")