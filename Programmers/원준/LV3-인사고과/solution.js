function solution(scores) {
  const userScore = scores[0][0] + scores[0][1];
  const newScore = scores
    .map((score, idx) => [...score, idx])
    .sort((a, b) => b[0] - a[0] || a[1] - b[1])
    .filter((item) => item[0] + item[1] >= userScore);
  const finalScore = [];
  let isIn = false;
  let count = 0;

  let [stdWorkScore, stdPartnerScore] = [0, 0];

  for (const [workScore, partnerScore, idx] of newScore) {
    if (partnerScore < stdPartnerScore) {
      if (workScore !== stdWorkScore) {
        continue;
      } else {
        finalScore.push([workScore, partnerScore, idx]);
        if (idx === 0) isIn = true;
      }
    } else {
      finalScore.push([workScore, partnerScore, idx]);
      stdPartnerScore = finalScore[finalScore.length - 1][1];
      stdWorkScore = finalScore[finalScore.length - 1][0];

      if (idx === 0) isIn = true;
    }
  }

  if (!isIn) return -1;

  const result = finalScore.reduce((finalResult, current) => {
    const score = parseInt(current[0]) + parseInt(current[1]);

    if (!finalResult.hasOwnProperty(score)) {
      finalResult[score] = [];
    }

    finalResult[score].push(current[2]);
    return finalResult;
  }, {});

  const finalResult = Object.keys(result)
    .map((value) => [parseInt(value), result[value]])
    .sort((a, b) => b[0] - a[0]);

  for (let i = 0; i < finalResult.length; i++) {
    if (finalResult[i][1].findIndex((item) => item === 0) !== -1) {
      count += 1;
      return count;
    } else {
      count += finalResult[i][1].length;
    }
  }
}

const scores = [
  [2, 2],
  [1, 4],
  [3, 2],
  [3, 2],
  [2, 1],
];
solution(scores);
