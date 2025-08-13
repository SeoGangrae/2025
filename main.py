import streamlit as st
import os

# 페이지 설정
st.set_page_config(page_title="MBTI 성격 특징 & 색깔 추천 💖", page_icon="🎯")

# 제목
st.markdown("<h1 style='text-align: center;'>🌈 MBTI 성격 특징 & 색깔 추천 + 캐릭터 🎨</h1>", unsafe_allow_html=True)

# MBTI 데이터 (팩트 특징 + 색상 + 캐릭터 로컬 이미지)
mbti_data = {
    "ISTJ": {"fact": "📚 책임감이 강하고 📏 체계적인 현실주의자", "color": "#4682B4", "img": "images/istj.png"},
    "ENFP": {"fact": "🔥 열정적이고 💡 창의적인 아이디어 뱅크", "color": "#FF69B4", "img": "images/enfp.png"},
    "INTJ": {"fact": "🧠 전략적이고 📊 독립적인 계획가", "color": "#6A5ACD", "img": "images/intj.png"},
    # ... 16개 MBTI 모두 추가 가능
}

# MBTI 선택
selected_mbti = st.selectbox("📌 당신의 MBTI를 선택하세요", list(mbti_data.keys()))

if selected_mbti:
    info = mbti_data[selected_mbti]

    st.markdown(f"<h2 style='text-align: center;'>✨ {selected_mbti} ✨</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px;'>{info['fact']}</p>", unsafe_allow_html=True)

    # 색깔 박스
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

    # 캐릭터 이미지
    img_path = info["img"]
    if os.path.exists(img_path):
        st.image(img_path, caption=f"{selected_mbti} 캐릭터 예시", use_column_width=True)
    else:
        st.warning("❌ 캐릭터 이미지를 찾을 수 없습니다. 'images' 폴더에 넣어주세요.")

    st.markdown("🌟" * 30)
    st.success("✨ 오늘 하루도 당신의 색처럼 빛나길 바랍니다! ✨")
    st.markdown("🌟" * 30)

