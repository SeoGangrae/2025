import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 성격 특징 & 색깔 추천 💖", page_icon="🎯")

# 제목
st.markdown("<h1 style='text-align: center;'>🌈 MBTI 성격 특징 & 색깔 추천 🎨</h1>", unsafe_allow_html=True)
st.write("당신의 MBTI를 선택하면 ✨ 팩트 특징 ✨과 잘 어울리는 🎯 색깔을 알려드려요!")

# MBTI 데이터 (팩트 특징 + 색상 + 추가 특징)
mbti_data = {
    "ISTJ": {
        "fact": "📚 책임감이 강하고 📏 체계적인 현실주의자",
        "color": "#4682B4",
        "details": [
            "계획을 세우고 지키는 걸 좋아함",
            "약속을 어기는 걸 싫어함",
            "디테일에 강함"
        ]
    },
    "ENFP": {
        "fact": "🔥 열정적이고 💡 창의적인 아이디어 뱅크",
        "color": "#FF69B4",
        "details": [
            "새로운 사람 만나는 걸 즐김",
            "아이디어가 넘쳐흐름",
            "즉흥적인 여행이나 활동을 좋아함"
        ]
    },
    "INTJ": {
        "fact": "🧠 전략적이고 📊 독립적인 계획가",
        "color": "#6A5ACD",
        "details": [
            "목표를 세우고 달성하는 데 집중함",
            "혼자서 문제 해결하는 걸 선호",
            "감정보다 논리를 중시함"
        ]
    },
    "INFP": {
        "fact": "💭 가치와 신념을 중시하는 🌈 이상주의자",
        "color": "#FFB6C1",
        "details": [
            "자신만의 가치관이 확고함",
            "타인의 감정을 잘 공감함",
            "혼자만의 시간을 소중히 여김"
        ]
    }
    # 나머지 MBTI도 같은 형식으로 추가 가능
}

# MBTI 선택
selected_mbti = st.selectbox("📌 당신의 MBTI를 선택하세요", list(mbti_data.keys()))

# 결과 표시
if selected_mbti:
    info = mbti_data[selected_mbti]

    # MBTI 제목
    st.markdown(f"<h2 style='text-align: center;'>✨ {selected_mbti} ✨</h2>", unsafe_allow_html=True)

    # 한 줄 특징
    st.markdown(f"<p style='text-align: center; font-size: 20px;'>{info['fact']}</p>", unsafe_allow_html=True)

    # 추천 색깔 박스
    st.markdown(
        f"""
        <div style='
            background-color:{info['color']};
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:20px;
            color:white;
            font-weight:bold;
            margin-top:20px;
        '>
            🎨 추천 색깔 : {info['color']} 💖
        </div>
        """,
        unsafe_allow_html=True
    )

    # 세부 특징 리스트
    st.markdown("#### 📌 더 많은 팩트 특징")
    for idx, detail in enumerate(info["details"], start=1):
        st.write(f"{idx}. {detail}")
