import streamlit as st

def count_claps(number):
    count = sum(1 for digit in str(number) if digit in ['3', '6', '9'])
    return '짝' * count if count > 0 else str(number)

def is_correct_response(number, response):
    return count_claps(number) == response.strip()

def next_turn():
    st.session_state.turn = "user" if st.session_state.turn == "ai" else "ai"
    st.session_state.current_number += 1

# 세션 상태 초기화
if "turn" not in st.session_state:
    st.session_state.turn = "user"
    st.session_state.current_number = 1
    st.session_state.game_over = False
    st.session_state.logs = []

st.title("3, 6, 9 게임 🎮")

if st.session_state.game_over:
    st.error("❌ 게임 오버!")
    if st.button("🔄 다시 시작하기"):
        st.session_state.turn = "user"
        st.session_state.current_number = 1
        st.session_state.game_over = False
        st.session_state.logs = []
    st.stop()

st.w



