function solution(n, info) {
  const ryanInfo = Array(11).fill(0);
  let maxDiff = 0;
  let result = [-1];

  function getDiff() {
    let diff = 0;
    for (let i = 0; i < 11; i++) {
      if (info[i] === 0 && ryanInfo[i] === 0) {
        continue;
      } else if (info[i] < ryanInfo[i]) {
        diff += 10 - i;
      } else {
        diff -= 10 - i;
      }
    }
    return diff;
  }

  function DFS(idx, arrow) {
    if (arrow === 0) {
      const diff = getDiff();
      if (maxDiff < diff) {
        maxDiff = diff;
        result = [...ryanInfo];
      }
      return;
    }

    if (idx === 11) return;

    for (let i = arrow; i >= 0; i--) {
      ryanInfo[10 - idx] += i;
      DFS(idx + 1, arrow - i);
      ryanInfo[10 - idx] -= i;
    }
  }

  DFS(0, n);

  return result;
}

const n = 5;
const info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0];

solution(n, info);
