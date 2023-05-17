function solution(board) {
  const n = board.length;
  const newBoard = Array.from(Array(n + 2), () => Array(n + 2).fill(0));
  const dangerArea = new Set();

  const dx = [0, -1, 0, 1, -1, -1, 1, 1];
  const dy = [1, 0, -1, 0, -1, 1, -1, 1];

  let start = 1;

  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      newBoard[i][j] = start++;
    }
  }

  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      if (board[i - 1][j - 1] === 1) {
        dangerArea.add(newBoard[i][j]);
        for (let k = 0; k < 8; k++) {
          let x = i + dx[k];
          let y = j + dy[k];

          if (newBoard[x][y] !== 0) {
            dangerArea.add(newBoard[x][y]);
          }
        }
      }
    }
  }

  return n * n - dangerArea.size;
}

solution([
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
]);
