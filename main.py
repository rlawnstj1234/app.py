import streamlit as st
import random

def count_claps(number):
    count = sum(1 for digit in str(number) if digit in ['3', '6', '9'])
    return '짝' * count if count > 0 else str(number)

def is_correct_response(number, response):
    return count_claps(number) == response.strip()

def next_turn(current_turn):
    return "user" if current_turn == "ai" else "ai"

# 초기 상태 설정
if "turn" not in st.session_state:
    st.session_state.turn = "user"
    st.session_state.current_number = 1
    st.session_state.game_over = False
    st.session_state.logs = []

st.title("3, 6, 9 게임 🤖🧑‍💻")

if st.session_state.game_over:
    st.error("❌ 게임 오버!")
    if st.button("다시 시작하기"):
        st.session_state.turn = "user"
        st.session_state.current_number = 1
        st.session_state.game_over = False
        st.session_state.logs = []
    st.stop()

st.write(f"현재 숫자: **{st.session_state.current_number}**")
st.write(f"턴: **{'사용자' if st.session_state.turn == 'user' else 'AI'}**")

# 사용자 차례
if st.session_state.turn == "user":
    user_input = st.text_input("당신의 응답을 입력하세요 (예: 1, 짝, 짝짝 등):", key=st.session_state.current_number)

    if st.button("제출"):
        if is_correct_response(st.session_state.current_number, user_input):
            st.success("✅ 정답입니다!")
            st.session_state.logs.append(f"👤 사용자: {user_input}")
            st.session_state.current_number += 1
            st.session_state.turn = "ai"
        else:
            st.session_state.logs.append(f"👤 사용자 (오답): {user_input}")
            st.session_state.game_over = True

# AI 차례
elif st.session_state.turn == "ai":
    ai_answer = count_claps(st.session_state.current_number)
    st.session_state.logs.append(f"🤖 AI: {ai_answer}")
    st.success(f"AI 응답: {ai_answer}")
    st.session_state.current_number += 1
    st.session_state.turn = "user"

# 로그 표시
st.write("---")
st.write("### 게임 로그")
for log in st.session_state.logs[::-1]:
    st.write(log)
