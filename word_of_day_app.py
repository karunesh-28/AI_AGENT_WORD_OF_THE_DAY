import streamlit as st
import datetime

# Sample word list
word_list = [
    {"word": "serendipity", "definition": "The occurrence of events by chance in a happy or beneficial way.",
     "example": "Finding that book in the attic was pure serendipity."},
    {"word": "elated", "definition": "Ecstatically happy.",
     "example": "She was elated at the news of her promotion."},
    {"word": "resilient", "definition": "Able to withstand or recover quickly from difficult conditions.",
     "example": "The community was resilient in the face of the flood."},
    {"word": "eloquent", "definition": "Fluent or persuasive in speaking or writing.",
     "example": "He gave an eloquent speech at the ceremony."},
    {"word": "solitude", "definition": "The state or situation of being alone.",
     "example": "She savored the solitude of the forest retreat."},
    {"word": "vivacious", "definition": "Attractively lively and animated.",
     "example": "Her vivacious personality made her popular."},
    {"word": "empathy", "definition": "The ability to understand and share the feelings of another.",
     "example": "She showed great empathy toward the grieving family."},
    {"word": "tranquil", "definition": "Free from disturbance; calm.",
     "example": "The tranquil lake reflected the mountains perfectly."},
    {"word": "ephemeral", "definition": "Lasting for a very short time.",
     "example": "The beauty of the sunset was ephemeral."},
    {"word": "meticulous", "definition": "Showing great attention to detail; very careful and precise.",
     "example": "He kept meticulous records of every expense."}
]

def get_word_by_date(date_obj):
    base_date = datetime.date(2024, 1, 1)
    index = (date_obj - base_date).days % len(word_list)
    return word_list[index]

# UI starts here
st.set_page_config(page_title="Word of the Day", page_icon="📖")
st.title("📚 Word of the Day AI Agent")

mode = st.radio("Choose how to select the date:", ["Yesterday", "Today", "Tomorrow", "Pick a date manually"])

# Determine selected date
if mode == "Pick a date manually":
    selected_date = st.date_input("📅 Select a date:", value=datetime.date.today())
else:
    offset = {"Yesterday": -1, "Today": 0, "Tomorrow": 1}[mode]
    selected_date = datetime.date.today() + datetime.timedelta(days=offset)

# Get word for that date
word_data = get_word_by_date(selected_date)

# Display
st.markdown(f"### 📅 Date: `{selected_date}`")
st.markdown(f"#### 🗣️ Word: `{word_data['word'].capitalize()}`")
st.markdown(f"**📖 Definition:** {word_data['definition']}")
st.markdown(f"**✍️ Example:** _{word_data['example']}_")

st.caption("Powered by Word Agent • Streamlit Frontend")
