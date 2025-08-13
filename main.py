import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 성격 특징 & 색깔 추천 💖", page_icon="🎯")

# 제목
st.markdown("<h1 style='text-align: center;'>🌈 MBTI 성격 특징 & 색깔 추천 + 캐릭터 🎨</h1>", unsafe_allow_html=True)
st.write("당신의 MBTI를 선택하면 ✨ 팩트 특징 ✨과 잘 어울리는 🎯 색깔, 그리고 관련 캐릭터를 알려드려요!")

# MBTI 데이터 (팩트 특징 + 색상 + 캐릭터 이미지 URL)
mbti_data = {
    "ISTJ": {"fact": "📚 책임감이 강하고 📏 체계적인 현실주의자", "color": "#4682B4",
             "img": "https://i.imgur.com/F4p5RrC.png"},  # 예시 캐릭터
    "ISFJ": {"fact": "💝 배려심 깊고 🛡️ 사람을 잘 챙기는 수호자", "color": "#8FBC8F",
             "img": "https://i.imgur.com/yYcUeXj.png"},
    "INFJ": {"fact": "🔮 통찰력 있고 💡 이상주의적인 조언자", "color": "#9370DB",
             "img": "https://i.imgur.com/9mM3h0D.png"},
    "INTJ": {"fact": "🧠 전략적이고 📊 독립적인 계획가", "color": "#6A5ACD",
             "img": "https://i.imgur.com/7Q9EItw.png"},
    "ISTP": {"fact": "🛠️ 문제 해결 능력이 뛰어난 🔍 실용주의자", "color": "#2F4F4F",
             "img": "https://i.imgur.com/Z8k9C7j.png"},
    "ISFP": {"fact": "🎨 감성적이고 🌺 따뜻한 모험가", "color": "#FFDAB9",
             "img": "https://i.imgur.com/0DkBbWs.png"},
    "INFP": {"fact": "💭 가치와 신념을 중시하는 🌈 이상주의자", "color": "#FFB6C1",
             "img": "https://i.imgur.com/wcZATUR.png"},
    "INTP": {"fact": "📖 논리적이고 🔍 창의적인 사색가", "color": "#708090",
             "img": "https://i.imgur.com/tZ5X6ho.png"},
    "ESTP": {"fact": "🏍️ 모험심이 강하고 ⚡ 활동적인 사업가", "color": "#FF4500",
             "img": "https://i.imgur.com/Mc0EScR.png"},
    "ESFP": {"fact": "🎉 사교적이고 🌟 에너지가 넘치는 엔터테이너", "color": "#FFA500",
             "img": "https://i.imgur.com/At0kA2r.png"},
    "ENFP": {"fact": "🔥 열정적이고 💡 창의적인 아이디어 뱅크", "color": "#FF69B4",
             "img": "https://i.imgur.com/pmd4RGy.png"},
    "ENTP": {"fact": "⚔️ 도전적이고 😏 재치 있는 토론가", "color": "#FF6347",
             "img": "https://i.imgur.com/BqfRL7H.png"},
    "ESTJ": {"fact": "🗂️ 조직적이고 🏆 리더십 있는 관리자", "color": "#4682B4",
             "img": "https://i.imgur.com/ebm7nyx.png"},
    "ESFJ": {"fact": "🤝 친절하고 🌿 조화를 중시하는 외교관", "color": "#98FB98",
             "img": "https://i.imgur.com/kqg3ftn.png"},
    "ENFJ": {"fact": "🌟 영감을 주고 🤗 이끄는 카리스마 리더", "color": "#DA70D6",
             "img": "https://i.imgur.com/6D7XcHi.png"},
    "ENTJ": {"fact": "🚀 목표 지향적이고 📈 조직을 이끄는 지휘관", "color": "#8B0000",
             "img": "https://i.imgur.com/VqfUVYi.png"},
}

# MBTI 선택
selected_mbti = st.selectbox("📌 당신의 MBTI를 선택하세요", list(mbti_data.keys()))

# 결과 표시
if selected_mbti:
    info = mbti_data[selected_mbti]

    # MBTI 이름
    st.markdown(f"<h2 style='text-align: center;'>✨ {selected_mbti} ✨</h2>", unsafe_allow_html=True)

    # 특징
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

    # 캐릭터 이미지 표시
    st.image(info["img"], caption=f"{selected_mbti} 캐릭터 예시", use_column_width=True)

    # 장식 이모지
    st.markdown("🌟" * 30)
    st.success("✨ 오늘 하루도 당신의 색처럼 빛나길 바랍니다! ✨")
    st.markdown("🌟" * 30)
