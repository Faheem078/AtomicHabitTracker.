import streamlit as st

# Page config
st.set_page_config(page_title="Atomic Habits Tracker", page_icon="📈")

# Initialize session state
if "habits" not in st.session_state:
    st.session_state.habits = {}

# Custom styling
st.markdown("""
    <style>
    .habit-box {
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        color: white;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>📈 Atomic Habits Tracker</h1>", unsafe_allow_html=True)

# Add habit
habit = st.text_input("Enter a habit")

if st.button("Add Habit"):
    if habit:
        st.session_state.habits[habit] = 0
        st.success(f"Added: {habit}")
    else:
        st.warning("Enter a valid habit")

# Show habits
if st.session_state.habits:
    selected = st.selectbox("Select Habit", list(st.session_state.habits.keys()))
    
    if st.button("Mark Done ✅"):
        st.session_state.habits[selected] += 1

    # Display all habits
    for h, count in st.session_state.habits.items():
        color = "#4CAF50" if count > 0 else "#555"
        
        st.markdown(f"""
            <div class="habit-box" style="background:{color};">
                <b>{h}</b><br>
                Completed: {count} times
            </div>
        """, unsafe_allow_html=True)