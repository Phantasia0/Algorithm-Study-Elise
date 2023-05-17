# solution.md 가이드 폼

## 문제 이름과 링크

- [인사고과](https://school.programmers.co.kr/learn/courses/30/lessons/152995)
- Level 3

## 풀이에 관련된 주된 이론

- 그리디처럼 접근하는 구현
- 여러가지 정렬과 데이터화

## 풀이 방법 (생각의 Flow 방식으로 글 작성)

- 가장 핵심은 초기 scores 데이터를 그리디적으로 정렬을 시키는 것이다.
- 이후에는 문제에서 주어진대로 구현해나가면 된다.

## 어려웠던 이유 (푸는데 어려웠다면 작성)

- 처음에는

```
finalResult[i][1].find((item)=>item === 0)
```

- 하고 풀다가 왜 안나오지 했다가 0은 falsy한 값인데 당연히 false 걸리는걸 미쳐 신경쓰지 못했었다.
- 이후 findIndex로 고쳐서 필터하였다.

- 이 부분도 테스트케이스 21에서 시간초과가 나버려서, 이렇게 수정한 것이다.

```
  const result = finalScore.reduce((finalResult, current) => {
    const score = parseInt(current[0]) + parseInt(current[1]);

    if (!finalResult.hasOwnProperty(score)) {
      finalResult[score] = [];
    }

    finalResult[score].push(current[2]);
    return finalResult;
  }, {});
```

- 맨 처음에는 리액트적으로 풀려다가,

```
const result = finalScore
    .map((value) => [parseInt(value[0]) + parseInt(value[1]), value[2]])
    .reduce((finalResult, current) => {
      const key = current[0].toString();
      finalResult[key] = [...(finalResult[key] || []), current[1]];
      return finalResult;
```

- 이렇게 풀었었는데, 시간복잡도를 어디서 많이 잡아먹는지에 관해 이곳저곳 수정하는데 시간이 걸렸다.
- 또한,

```
const userScore = scores[0][0] + scores[0][1];
  const newScore = scores
    .map((score, idx) => [...score, idx])
    .sort((a, b) => b[0] - a[0] || a[1] - b[1])
    .filter((item) => item[0] + item[1] >= userScore);
```

- 이 부분도, 원래 userScore를 안쓰고 filter도 안했었는데, 시간초과 난거를 해결하기 위해
- 추가하였고, 정답처리 되는 테스트케이스들의 시간이 거의 2배 가량 줄어들었다.

## 개선 방안 (효율성 테스트 결과가 실패했거나 더 좋은 아이디어가 있을 경우 작성)

- 알고리즘에 대한 감 대신, 몸에 배긴 프론트적인 감으로 풀다가 원활히 풀지 못하였다.
- 다양한 유형의 문제를 집중적으로 하면 좀더 알고리즘적으로 풀 수 있을 것 같은데...
- 프론트 해야할게 너무 많다.
