import streamlit as st
import random
import datetime

# 영화/드라마 데이터 및 부가정보
movies = {
    "액션": {
        "신남": [
            "어벤져스: 엔드게임", "미션 임파서블: 폴아웃", "분노의 질주", "킹스맨", 
            "존 윅", "매드맥스: 분노의 도로", "범죄도시", "베테랑", "신세계",
            "Fight", "Mickey 17", "Omniscient Reader: The Prophecy"
        ],
        "우울": [
            "다크 나이트", "로건", "블레이드 러너 2049", "아저씨", "남한산성", 
            "Harbin", "Yadang: The Snitch"
        ]
    },
    "코미디": {
        "신남": [
            "극한직업", "맨 인 블랙", "행오버", "쥬만지", "수상한 그녀", 
            "7번방의 선물", "국제시장", "Hitman 2", "Hi-Five", "My Daughter Is a Zombie"
        ],
        "우울": [
            "웰컴 투 동막골", "써니", "헬로우 고스트", "미나문방구"
        ]
    },
    "드라마": {
        "신남": [
            "포레스트 검프", "굿 윌 헌팅", "라라랜드", "인생은 아름다워", 
            "기생충", "인터스텔라", "우리들의 블루스(드라마)", "응답하라 1988(드라마)"
        ],
        "우울": [
            "레버넌트", "죽은 시인의 사회", "쇼생크 탈출", "미나리", 
            "괴물(드라마)", "나의 아저씨(드라마)", "Harbin", "Yadang: The Snitch"
        ]
    },
    "공포/스릴러": {
        "신남": [
            "겟 아웃", "인시디어스", "컨저링", "곡성", "부산행"
        ],
        "우울": [
            "조커", "그것", "미드소마", "스플릿", "살인의 추억", "Dark Nuns"
        ]
    },
    "로맨스": {
        "신남": [
            "타이타닉", "노트북", "어바웃 타임", "비포 선라이즈", 
            "500일의 썸머", "건축학개론", "지금, 만나러 갑니다", "너의 결혼식"
        ],
        "우울": [
            "이터널 선샤인", "브로크백 마운틴", "결혼 이야기", 
            "헤어질 결심", "시월애"
        ]
    },
    "SF/판타지": {
        "신남": [
            "스타워즈: 깨어난 포스", "가디언즈 오브 갤럭시", "닥터 스트레인지", 
            "아바타", "승리호", "듄", "Mickey 17", "Omniscient Reader: The Prophecy"
        ],
        "우울": [
            "블레이드 러너 2049", "엑스 마키나", "그래비티", "컨택트", "설국열차"
        ]
    }
}

# 영화/드라마 부가정보
movie_info = {
    "응답하라 1988(드라마)": {
        "등장인물": ["덕선", "정환", "택", "보라", "선우"],
        "줄거리": "1988년 서울 쌍문동을 배경으로 다섯 친구와 가족들의 따뜻하고 웃픈 일상을 그린 드라마."
    },
    "우리들의 블루스(드라마)": {
        "등장인물": ["한수", "연희", "정호", "영희"],
        "줄거리": "제주도를 배경으로 다양한 사람들의 삶과 사랑, 갈등을 감성적으로 그려낸 옴니버스 드라마."
    },
    "기생충": {
        "등장인물": ["기택", "연교", "기우", "기정", "박 사장 가족"],
        "줄거리": "가난한 가족이 부잣집에 들어가면서 벌어지는 블랙코미디 사회극."
    },
    "타이타닉": {
        "등장인물": ["잭", "로즈"],
        "줄거리": "1912년 타이타닉 호를 배경으로 한 젊은 남녀의 사랑과 비극."
    },
    "노트북": {
        "등장인물": ["노아", "앨리"],
        "줄거리": "두 연인이 사회적 배경과 시간의 간극을 극복하며 겪는 사랑 이야기."
    }
    # 필요하면 여기 추가로 더 넣으면 됨
}

st.title("🎬 오늘의 무드 플레이리스트")

# 입력 받기
genre = st.selectbox("보고 싶은 장르를 선택하세요", list(movies.keys()))
mood = st.selectbox("현재 기분을 선택하세요", ["신남", "우울"])

# 선택 기반 추천
if st.button("추천 받기"):
    recommendations = movies[genre][mood]
    choice = random.choice(recommendations)
    st.success(f"오늘의 추천 작품 🎥: **{choice}**")
    st.write("👉 같은 분위기의 다른 추천 리스트:")
    for movie in recommendations:
        st.write(f"- {movie}")
    
    # 부가정보 출력
    info = movie_info.get(choice)
    if info:
        st.write(f"**등장인물:** {', '.join(info['등장인물'])}")
        st.write(f"**줄거리:** {info['줄거리']}")

# 오늘의 추천 영화 (매일 고정)
all_movies = []
for genre_movies in movies.values():
    for mood_movies in genre_movies.values():
        all_movies.extend(mood_movies)

today = datetime.date.today()
random.seed(today.toordinal())
daily_movie = random.choice(all_movies)

st.info(f"📅 {today} 오늘의 추천 영화는 🎬 **{daily_movie}** 입니다!")

# 오늘의 추천 영화 부가정보
info_daily = movie_info.get(daily_movie)
if info_daily:
    st.write(f"**등장인물:** {', '.join(info_daily['등장인물'])}")
    st.write(f"**줄거리:** {info_daily['줄거리']}")
