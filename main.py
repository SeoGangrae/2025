import streamlit as st

# 앱 제목
st.title("MBTI 성격 특징 & 색깔 추천")

# MBTI 데이터 (팩트 특징 + 색상)
mbti_data = {
    "ISTJ": {"fact": "책임감이 강하고 체계적이며 현실적인 성향을 가짐", "color": "#4682B4"},
    "ISFJ": {"fact": "배려심이 깊고 사람을 잘 챙기며 헌신적인 성격", "color": "#8FBC8F"},
    "INFJ": {"fact": "깊은 통찰력을 바탕으로 타인을 이해하고 돕는 성향", "color": "#9370DB"},
    "INTJ": {"fact": "전략적으로 계획을 세우며 독립적인 판단을 선호", "color": "#6A5ACD"},
    "ISTP": {"fact": "문제 해결에 능숙하며 분석적이고 실용적인 성향", "color": "#2F4F4F"},
    "ISFP": {"fact": "따뜻하고 온화하며 감각적인 아름다움을 선호", "color": "#FFDAB9"},
    "INFP": {"fact": "가치와 신념을 중요시하며 이상을 추구", "color": "#FFB6C1"},
    "INTP": {"fact": "논리적이고 창의적인 아이디어를 탐구하는 성향", "color": "#708090"},
    "ESTP": {"fact": "모험심이 강하고 활동적이며 즉흥적인 행동을 선호", "color": "#FF4500"},
    "ESFP": {"fact": "사람들과 어울리는 것을 즐기고 밝고 에너지가 넘침", "color": "#FFA500"},
    "ENFP": {"fact": "창의적이고 열정적이며 자유로운 사고를 중시", "color": "#FF69B4"},
    "ENTP": {"fact": "도전적이며 재치 있고 다양한 가능성을 탐험", "color": "#FF6347"},
    "ESTJ": {"fact": "조직적이고 현실적인 해결책을 제시하는 리더", "color": "#4682B4"},
    "ESFJ": {"fact": "사람들을 잘 돌보고 협력과 조화를 중시", "color": "#98FB98"},
    "ENFJ": {"fact": "사람들에게 영감을 주고 이끄는 능력이 있음", "color": "#DA70D6"},
    "ENTJ": {"fact": "목표 지향적이며 계획적으로 조직을 이끄는 리더", "color": "#8B0000"},
}

# 드롭다운으로 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", list(mbti_data.keys()))

# 선택 결과 출력
if selected_mbti:
    info = mbti_data[selected_mbti]
    st.subheader(f"MBTI: {selected_mbti}")
    st.write(f"**팩트 특징:** {info['fact']}")
    st.markdown(
        f"<div style='background-color:{info['color']}; padding:20px; border-radius:10px; color:white;'>"
        f"<b>추천 색깔:</b> {info['color']}</div>",
        unsafe_allow_html=True
    )

