import { useState } from "react";
import { motion } from "framer-motion";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function MovieRecommender() {
  const [genre, setGenre] = useState("");
  const [mood, setMood] = useState("");
  const [recommendation, setRecommendation] = useState(null);
  const [bgColor, setBgColor] = useState("bg-gray-100");

  const movies = {
    "공포": {
      "스릴 넘치게": "컨저링 (The Conjuring)",
      "무섭지만 재밌게": "겟 아웃 (Get Out)",
      "긴장되게": "인시디어스 (Insidious)",
    },
    "로맨스": {
      "설레게": "라라랜드 (La La Land)",
      "따뜻하게": "어바웃 타임 (About Time)",
      "잔잔하게": "비포 선라이즈 (Before Sunrise)",
    },
    "액션": {
      "통쾌하게": "존 윅 (John Wick)",
      "화끈하게": "매드맥스: 분노의 도로 (Mad Max: Fury Road)",
      "스릴 있게": "인셉션 (Inception)",
    },
  };

  const bgThemes = {
    "공포": "bg-red-900 text-white",
    "로맨스": "bg-pink-200 text-black",
    "액션": "bg-yellow-400 text-black",
    "기본": "bg-gray-100 text-black",
  };

  const handleRecommend = () => {
    if (genre && mood) {
      setRecommendation(movies[genre][mood]);
      setBgColor(bgThemes[genre] || bgThemes["기본"]);
    }
  };

  return (
    <motion.div
      className={`min-h-screen flex flex-col items-center justify-center transition-colors duration-700 ${bgColor}`}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      <Card className="w-[400px] shadow-xl rounded-2xl p-6">
        <CardContent className="flex flex-col gap-4">
          <h1 className="text-xl font-bold text-center">🎬 영화 추천기</h1>

          {/* 장르 선택 */}
          <select
            value={genre}
            onChange={(e) => setGenre(e.target.value)}
            className="border p-2 rounded-lg"
          >
            <option value="">장르 선택</option>
            <option value="공포">공포</option>
            <option value="로맨스">로맨스</option>
            <option value="액션">액션</option>
          </select>

          {/* 기분 선택 */}
          {genre && (
            <select
              value={mood}
              onChange={(e) => setMood(e.target.value)}
              className="border p-2 rounded-lg"
            >
              <option value="">기분 선택</option>
              {Object.keys(movies[genre]).map((m) => (
                <option key={m} value={m}>{m}</option>
              ))}
            </select>
          )}

          <Button onClick={handleRecommend} className="mt-2">추천받기</Button>

          {/* 추천 결과 */}
          {recommendation && (
            <motion.div
              className="mt-4 text-center text-lg font-semibold"
              initial={{ scale: 0.5, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.5 }}
            >
              👉 오늘의 추천 영화: {recommendation}
            </motion.div>
          )}
        </CardContent>
      </Card>
    </motion.div>
  );
}

