function solution(n, wires) {
  //송전탑개수 2~100
  const dict = {};
  const answer = [];

  for (let wire of wires) {
    !(wire[0] in dict)
      ? (dict[wire[0]] = [wire[1]])
      : dict[wire[0]].push(wire[1]);

    !(wire[1] in dict)
      ? (dict[wire[1]] = [wire[0]])
      : dict[wire[1]].push(wire[0]);
  }

  console.log(dict);

  for (let wire of wires) {
    const [start, end] = wire;
    const stack = [...dict[start]];
    const visited = {};
    let count = 1;

    // 시작과 끝점
    visited[start] = true;
    visited[end] = true;

    while (stack.length !== 0) {
      const temp = stack.pop();
      if (!visited[temp]) {
        visited[temp] = true;
        stack.push(...dict[temp]);
        count += 1;
      }
    }
    console.log(count);
    answer.push(Math.abs(count * 2 - n));
  }
  console.log(answer);
  return Math.min(...answer);
}

solution(9, [
  [1, 3],
  [2, 3],
  [3, 4],
  [4, 5],
  [4, 6],
  [4, 7],
  [7, 8],
  [7, 9],
]);
