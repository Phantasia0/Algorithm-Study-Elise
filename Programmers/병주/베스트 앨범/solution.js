// https://school.programmers.co.kr/learn/courses/30/lessons/42579#

// 장르별로 가장 많이 재생된 노래를 두개씩 구성

function solution(genres, plays) {
  const table = new Map();

  genres.forEach((v, idx) => {
    const data = table.get(v) || { total: 0, songs: [] };

    table.set(v, {
      total: data.total + plays[idx],

      // 장르별 노래리스트 최대 두개까지
      // 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
      songs: [[plays[idx], idx], ...data.songs]
        .sort((a, b) => {
          b[0] === a[0] ? -1 : b[0] - a[0];
        })
        .slice(0, 2),
    });
  });

  console.log(
    table
    // [...table.entries()]
    //   .sort((a, b) => b[1].total - a[1].total)
    //   .flatMap((v) => v[1].songs)
    //   .map((v) => v[1])
  );

  return [...table.entries()]
    .sort((a, b) => b[1].total - a[1].total)
    .flatMap((v) => v[1].songs)
    .map((v) => v[1]);
}

console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);
