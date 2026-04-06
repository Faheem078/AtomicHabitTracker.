import streamlit as st
import datetime
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Atomic Habits Tracker", page_icon="⚡", layout="centered")

# Session state
if "habits" not in st.session_state:
    st.session_state.habits = {}

# Custom CSS (Grey + Neon Style)
st.markdown("""
<style>
body {
    background-color: #0f1117;
}
.title {
    text-align: center;
    font-size: 40px;
    color: #39ff14;
    font-weight: bold;
}
.habit-card {
    background: #1c1f26;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    box-shadow: 0 0 10px #39ff14;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">⚡ Atomic Habits Tracker</div>', unsafe_allow_html=True)

# Add Habit
new_habit = st.text_input("Add New Habit")

if st.button("Add Habit"):
    if new_habit:
        st.session_state.habits[new_habit] = {
            "dates": [],
            "streak": 0
        }
        st.success(f"Added: {new_habit}")
    else:
        st.warning("Enter a valid habit")

st.divider()

# Function to mark done
def mark_done(habit):
    today = str(datetime.date.today())
    data = st.session_state.habits[habit]

    if today not in data["dates"]:
        data["dates"].append(today)

        # Update streak
        if len(data["dates"]) >= 2:
            yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
            if yesterday in data["dates"]:
                data["streak"] += 1
            else:
                data["streak"] = 1
        else:
            data["streak"] = 1

# Display Habits
for habit, data in st.session_state.habits.items():
    with st.container():
        st.markdown('<div class="habit-card">', unsafe_allow_html=True)

        col1, col2 = st.columns([3,1])

        with col1:
            st.subheader(habit)
            st.write(f"🔥 Streak: {data['streak']} days")

        with col2:
            if st.button("✔️ Done", key=habit):
                mark_done(habit)

        # Graph
        if data["dates"]:
            dates = [datetime.datetime.strptime(d, "%Y-%m-%d") for d in data["dates"]]
            counts = list(range(1, len(dates) + 1))

            fig, ax = plt.subplots()
            ax.plot(dates, counts, marker='o')
            ax.set_title(f"{habit} Progress")
            ax.set_xlabel("Date")
            ax.set_ylabel("Completions")

            st.pyplot(fig)

        st.markdown('</div>', unsafe_allow_html=True)