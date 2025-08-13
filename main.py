import streamlit as st

# 제목
st.title("MBTI 성격 특징 & 색깔 추천")

# MBTI 데이터 (16가지)
mbti_data = {
    "ISTJ": {"desc": "신중하고 책임감 있는 현실주의자", "color": "#4682B4"},
    "ISFJ": {"desc": "헌신적이고 배려심 깊은 수호자", "color": "#8FBC8F"},
    "INFJ": {"desc": "통찰력 있고 이상주의적인 조언자", "color": "#9370DB"},
    "INTJ": {"desc": "전략적이고 독립적인 계획가", "color": "#6A5ACD"},
    "ISTP": {"desc": "차분하고 문제 해결에 능숙한 장인", "color": "#2F4F4F"},
    "ISFP": {"desc": "따뜻하고 예술적인 모험가", "color": "#FFDAB9"},
    "INFP": {"desc": "이상적이고 가치 중심적인 중재자", "color": "#FFB6C1"},
    "INTP": {"desc": "분석적이고 창의적인 사색가", "color": "#708090"},
    "ESTP": {"desc": "에너지 넘치고 모험을 즐기는 사업가", "color": "#FF4500"},
    "ESFP": {"desc": "사교적이고 활발한 엔터테이너", "color": "#FFA500"},
    "ENFP": {"desc": "열정적이고 창의적인 아이디어 뱅크", "color": "#FF69B4"},
    "ENTP": {"desc": "도전적이고 재치 있는 토론가", "color": "#FF6347"},
    "ESTJ": {"desc": "체계적이고 리더십 있는 관리자", "color": "#4682B4"},
    "ESFJ": {"desc": "친절하고 조화를 중시하는 외교관", "color": "#98FB98"},
    "ENFJ": {"desc": "영감을 주고 이끄는 카리스마 리더", "color": "#DA70D6"},
    "ENTJ": {"desc": "대담하고 목표 지향적인 지휘관", "color": "#8B0000"},
}

# 사용자 입력
user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INTJ)").upper()

# 결과 출력
if user_mbti:
    if user_mbti in mbti_data:
        info = mbti_data[user_mbti]
        st.subheader(f"MBTI: {user_mbti}")
        st.write(f"**특징:** {info['desc']}")
        st.markdown(
            f"<div style='background-color:{info['color']}; padding:20px; border-radius:10px; color:white;'>"
            f"<b>추천 색깔:</b> {info['color']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.error("올바른 MBTI를 입력해주세요. 예: INTJ, ENFP 등")
