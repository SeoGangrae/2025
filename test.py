import streamlit as st
import random
import datetime

st.set_page_config(page_title="오늘의 무드 플레이리스트", page_icon="🎬", layout="centered")

# --- 장르별/기분별 작품 목록 ---
movies = {
    "액션": {"신남": ["어벤져스: 엔드게임", "미션 임파서블: 폴아웃", "분노의 질주"],
            "설렘": ["킹스맨", "존 윅"],
            "유쾌함": ["범죄도시", "베테랑"],
            "감성": ["신세계", "매드맥스: 분노의 도로"],
            "긴장": ["다크 나이트", "로건"],
            "공포": ["블레이드 러너 2049"],
            "우울": ["남한산성"]},
    "코미디": {"신남": ["극한직업", "맨 인 블랙", "행오버"],
             "설렘": ["쥬만지", "수상한 그녀"],
             "유쾌함": ["7번방의 선물", "국제시장"],
             "감성": ["웰컴 투 동막골"],
             "긴장": ["맨 인 블랙"],
             "공포": ["쥬만지"],
             "우울": ["써니", "헬로우 고스트"]},
    "드라마": {"신남": ["포레스트 검프", "굿 윌 헌팅"],
             "설렘": ["라라랜드", "인생은 아름다워"],
             "유쾌함": ["기생충"],
             "감성": ["인터스텔라", "우리들의 블루스(드라마)", "응답하라 1988(드라마)"],
             "긴장": ["레버넌트"],
             "공포": ["레버넌트"],
             "우울": ["죽은 시인의 사회", "쇼생크 탈출", "미나리"]},
    "로맨스": {"신남": ["타이타닉", "노트북"],
             "설렘": ["어바웃 타임", "비포 선라이즈"],
             "유쾌함": ["500일의 썸머", "건축학개론"],
             "감성": ["지금, 만나러 갑니다", "너의 결혼식"],
             "긴장": ["이터널 선샤인"],
             "공포": ["브로크백 마운틴"],
             "우울": ["결혼 이야기", "헤어질 결심", "시월애"]},
    "SF/판타지": {"신남": ["스타워즈: 깨어난 포스", "가디언즈 오브 갤럭시"],
               "설렘": ["닥터 스트레인지", "아바타"],
               "유쾌함": ["승리호", "듄"],
               "감성": ["블레이드 러너 2049", "엑스 마키나"],
               "긴장": ["인터스텔라"],
               "공포": ["엑스 마키나"],
               "우울": ["그래비티", "컨택트", "설국열차"]},
    "공포/스릴러": {"신남": ["겟 아웃"],
                 "설렘": ["컨저링"],
                 "유쾌함": ["곡성"],
                 "감성": ["부산행"],
                 "긴장": ["그것", "미드소마", "스플릿"],
                 "공포": ["인시디어스", "컨저링"],
                 "우울": ["살인의 추억", "조커"]}
}

# --- 작품별 명대사 & 3줄 요약 ---
info = {
    "어벤져스: 엔드게임": {"quote": "“I love you 3000.”",
                         "syn": ["모든 것을 되돌리기 위한 마지막 작전",
                                 "히어로들이 시간 여행으로 인피니티 스톤 회수 도전",
                                 "희생과 팀워크의 완성으로 대서사 마무리"]},
    "미션 임파서블: 폴아웃": {"quote": "“운도 실력의 일부지.”",
                             "syn": ["핵 위협을 막기 위한 시간과의 레이스",
                                     "이단 헌트가 팀과 함께 전 세계 추격전",
                                     "절벽·헬기·도심 액션의 정점"]},
    "분노의 질주": {"quote": "“가족이 전부야.”",
                   "syn": ["스트리트 레이싱에서 시작된 패밀리 액션",
                           "스릴 넘치는 카체이싱과 팀플레이",
                           "의리와 배신 사이, 결국 남는 건 가족"]},
    "킹스맨": {"quote": "“Manners maketh man.”",
             "syn": ["영국 신사 스파이 조직의 비밀 미션",
                     "스타일리시한 액션과 유머",
                     "신입 요원의 성장 서사"]},
    "존 윅": {"quote": "“사람들이 나를 왜 무서워했는지 보여줄 시간이지.”",
            "syn": ["전설의 킬러가 복수를 위해 돌아오다",
                    "정교한 총격전과 근접 전투",
                    "룰로 움직이는 범죄 세계관"]},
    "매드맥스: 분노의 도로": {"quote": "“불멸을 꿈꿔라.”",
                            "syn": ["사막을 가르는 광기의 추격전",
                                    "퓨리오사와 맥스의 연합 탈출",
                                    "폭발적 비주얼과 리듬감"]},
    "범죄도시": {"quote": "“느그 서장은 어딨노?”",
               "syn": ["강력반의 통쾌한 소탕 작전",
                       "마동석표 핵주먹 액션",
                       "현실감 넘치는 범죄 활극"]},
    "베테랑": {"quote": "“우리가 돈이 없지 가오가 없냐.”",
             "syn": ["재벌 2세 악행을 쫓는 강력반",
                     "사이다 전개와 코믹 버디무비 감성",
                     "정의감 폭발 액션 드라마"]},
    "신세계": {"quote": "“너 나랑 일 하나 같이 하자.”",
             "syn": ["경찰과 조직 사이 잠입 수사",
                     "판이 커질수록 흔들리는 믿음",
                     "비극으로 흘러가는 느와르"]},
    "다크 나이트": {"quote": "“Why so serious?”",
                  "syn": ["조커의 혼돈이 고담을 뒤흔들다",
                          "영웅과 정의의 경계를 묻는 이야기",
                          "압도적 긴장감과 명연기"]},
    "로건": {"quote": "“가족… 그게 뭔지 이제 알 것 같아.”",
            "syn": ["지친 영웅의 마지막 여정",
                    "소녀를 지키기 위한 도주",
                    "잔혹하지만 따뜻한 이별"]},
    "블레이드 러너 2049": {"quote": "“Tears in rain.”",
                          "syn": ["복제인간의 존재와 기억의 의미",
                                  "황량한 미래 도시의 미스터리",
                                  "정체성을 찾아가는 여정"]},
    "헤어질 결심": {"quote": "“의심했는데… 사랑이었어.”",
                  "syn": ["형사와 용의자의 금지된 감정",
                          "의심과 사랑 사이의 긴장",
                          "끝내 바다로 사라진 비극적 결말"]},
    "인터스텔라": {"quote": "“사랑은 시간을 초월한다.”",
                  "syn": ["인류 생존을 위한 우주 탐사",
                          "블랙홀과 시간 왜곡의 드라마",
                          "부녀의 약속이 이끄는 기적"]},
    "라라랜드": {"quote": "“Here’s to the ones who dream.”",
                "syn": ["꿈과 사랑 사이의 선택",
                        "재즈와 댄스 넘버로 그린 로맨스",
                        "달콤쌉싸름한 엔딩"]}
}

# --- 기분별 배경 색상 (파스텔 톤) ---
mood_bg = {
    "신남": "#FFF9A5",      # 연노랑
    "설렘": "#FFB6C1",      # 연핑크
    "유쾌함": "#FFD8A8",    # 연주황
    "감성": "#ADD8E6",      # 연파랑
    "긴장": "#CDA4E8",      # 연보라
    "공포": "#F08080",      # 연붉은
    "우울": "#D3D3D3"       # 연회색
}

st.title("오늘의 무드 플레이리스트")

# --- 입력 UI ---
col1, col2 = st.columns(2)
with col1:
    genre = st.selectbox("🎬 장르", list(movies.keys()))
with col2:
    mood = st.selectbox("😊 현재 기분", list(mood_bg.keys()))

# --- 추천 로직 ---
if st.button("추천받기"):
    candidates = movies[genre].get(mood, [])
    if not candidates:
        st.warning("선택하신 조합은 아직 준비 중이에요. 다른 기분을 선택해 보세요!")
    else:
        with_info = [m for m in candidates if m in info]
        pool = with_info if with_info else candidates
        title = random.choice(pool)

        # 배경색 & 글씨 크기 CSS 적용
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {mood_bg.get(mood, "#FFFFFF")};
                transition: background-color 0.6s ease;
            }}
            .big-title {{
                font-size: 2.5em !important;
                font-weight: bold;
            }}
            .quote {{
                font-size: 1.5em !important;
                color: #333333;
            }}
            .synopsis {{
                font-size: 1.2em !important;
            }}
            </style>
            """, unsafe_allow_html=True
        )

        st.markdown(f"<div class='big-title'>오늘의 추천 작품: {title}</div>", unsafe_allow_html=True)

        if title in info:
            st.markdown("<div class='quote'>🎞️ 명대사: " + info[title]["quote"] + "</div>", unsafe_allow_html=True)
            st.markdown("<div class='synopsis'>📘 3줄 요약</div>", unsafe_allow_html=True)
            for line in info[title]["syn"]:
                st.markdown(f"<div class='synopsis'>- {line}</div>", unsafe_allow_html=True)
        else:
            st.info("해당 작품의 명대사/요약은 준비 중이에요!")

# --- 오늘의 추천 (날짜 고정) ---
all_titles = []
for g in movies.values():
    for lst in g.values():
        all_titles.extend(lst)

today = datetime.date.today()
random.seed(today.toordinal())
daily_pick = random.choice(all_titles)

st.divider()
st.caption(f"📅 오늘({today})의 고정 추천")
st.write(f"🎬 **{daily_pick}**")
if daily_pick in info:
    st.caption("한 줄 대사")
    st.write(f"“{info[daily_pick]['quote']}”")
