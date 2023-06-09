# solution.md 가이드 폼

## 문제 이름과 링크

- [가장 긴 팰린드롬](https://school.programmers.co.kr/learn/courses/30/lessons/12904)
- Level 3

## 풀이에 관련된 주된 이론

- 회문 로직
- 완전 탐색

## 풀이 방법 (생각의 Flow 방식으로 글 작성)

- 팰린드롬이란, 앞뒤를 뒤집어도 똑같은 문자열을

- 가장 긴 길이부터 탐색하여, 없다면 가장 짧은 회문인 1 리턴
- abacde 의 경우
- 1. abacde 검사 -> 만약 회문이라면 리턴
- 2. abacd / bacde 검사 -> 만약 회문이 나온다면 리턴
- 3. abac / bacd / acde 검사 -> 만약 회문이 나온다면 리턴
- 4. `aba` / bac / acd / cde 검사 -> 만약 회문이 나온다면 리턴
- `aba` 가 회문이므로 가장 긴 길이의 펠린드롬이 되고 이것을 리턴하면 된다.

## 어려웠던 이유 (푸는데 어려웠다면 작성)

- 이렇게 풀면 없다.
- 근데 시간복잡도가 `O(n^3)` 이다.
- 그런데 문제의 효율성은 이렇게 풀어도 효율성 테스트를 통과하도록 하였다.
- 만약 이렇게 풀면 통과 안되게, 즉 (`O(n^2)`) 시간 복잡도일때 효율성 테스트를 통과하게 만든다면,
- 그때는 어려워질 것 같다.

## 개선 방안 (효율성 테스트 결과가 실패했거나 더 좋은 아이디어가 있을 경우 작성)

- DP 접근으로 하면 `O(n^2)`가 나올 것 같다.
- 결국, DP로 접근해서 푸는게 더 개선된 풀이다.
