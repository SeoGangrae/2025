import streamlit as st
import random
import datetime

# 영화/드라마 데이터 (기분별)
movies = {
    "액션": {
        "신남": ["어벤져스: 엔드게임", "미션 임파서블: 폴아웃", "분노의 질주"],
        "설렘": ["킹스맨", "존 윅"],
        "유쾌함": ["범죄도시", "베테랑"],
        "감성": ["신세계", "매드맥스: 분노의 도로"],
        "긴장": ["다크 나이트", "로건"],
        "공포": ["블레이드 러너 2049"],
        "우울": ["남한산성", "Harbin"]
    },
    "코미디": {
        "신남": ["극한직업", "맨 인 블랙", "행오버"],
        "설렘": ["쥬만지", "수상한 그녀"],
        "유쾌함": ["7번방의 선물", "국제시장"],
        "감성": ["Hitman 2", "Hi-Five"],
        "긴장": ["My Daughter Is a Zombie"],
        "공포": ["웰컴 투 동막골"],
        "우울": ["써니", "헬로우 고스트", "미나문방구"]
    },
    "드라마": {
        "신남": ["포레스트 검프", "굿 윌 헌팅"],
        "설렘": ["라라랜드", "인생은 아름다워"],
        "유쾌함": ["기생충"],
        "감성": ["인터스텔라", "우리들의 블루스(드라마)"],
        "긴장": ["응답하라 1988(드라마)"],
        "공포": ["레버넌트"],
        "우울": ["죽은 시인의 사회", "쇼생크 탈출", "미나리"]
    },
    "로맨스": {
        "신남": ["타이타닉", "노트북"],
        "설렘": ["어바웃 타임", "비포 선라이즈"],
        "유쾌함": ["500일의 썸머", "건축학개론"],
        "감성": ["지금, 만나러 갑니다", "너의 결혼식"],
        "긴장": ["이터널 선샤인"],
        "공포": ["브로크백 마운틴"],
        "우울": ["결혼 이야기", "헤어질 결심", "시월애"]
    },
    "SF/판타지": {
        "신남": ["스타워즈: 깨어난 포스", "가디언즈 오브 갤럭시"],
        "설렘": ["닥터 스트레인지", "아바타"],
        "유쾌함": ["승리호", "듄"],
        "감성": ["Mickey 17", "Omniscient Reader: The Prophecy"],
        "긴장": ["블레이드 러너 2049"],
        "공포": ["엑스 마키나"],
        "우울": ["그래비티", "컨택트", "설국열차"]
    },
    "공포/스릴러": {
        "신남": ["겟 아웃", "인시디어스"],
        "설렘": ["컨저링"],
        "유쾌함": ["곡성"],
        "감성": ["부산행"],
        "긴장": ["그것", "미드소마"],
        "공포": ["스플릿"],
        "우울": ["살인의 추억", "Dark Nuns"]
    }
}

# 기분별 배경 색상
mood_bg_color = {
    "신남": "#FFF700",      # 노랑
    "설렘": "#FF69B4",      # 분홍
    "유쾌함": "#FFA500",    # 주황
    "감성": "#1E90FF",      # 파랑
    "긴장": "#800080",      # 보라
    "공포": "#8B0000",      # 진한 빨강
    "우울": "#A9A9A9"       # 회색
}

st.title("🎬 오늘의 무드 플레이리스트")

# 공통 기분 선택
mood_options = ["신남", "설렘", "유쾌함", "감성", "긴장", "공포", "우울"]
mood = st.selectbox("현재 기분을 선택하세요", mood_options)

# 장르 선택
genre = st.selectbox("보고 싶은 장르를 선택하세요", list(movies.keys()))

# 선택 기반 추천
if st.button("추천 받기"):
    recommendations = movies[genre].get(mood)
    if recommendations:
        choice = random.choice(recommendations)
        color = mood_bg_color.get(mood, "#FFFFFF")
        
        # 전체 페이지 배경 변경
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {color};
                transition: background-color 0.5s ease;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        
        st.success(f"오늘의 추천 작품 🎥: **{choice}**")
        st.write("👉 같은 분위기의 다른 추천 리스트:")
        for movie in recommendations:
            st.write(f"- {movie}")
    else:
        st.warning("죄송합니다. 선택하신 기분에 맞는 작품이 없습니다.")

# 오늘의 추천 영화 (매일 고정)
all_movies = []
for genre_movies in movies.values():
    for mood_movies in genre_movies.values():
        all_movies.extend(mood_movies)

today = datetime.date.today()
random.seed(today.toordinal())
daily_movie = random.choice(all_movies)

st.info(f"📅 {today} 오늘의 추천 영화는 🎬 **{daily_movie}** 입니다!")

