# solution.md 가이드 폼

## 문제 이름과 링크

- [양궁대회](https://school.programmers.co.kr/learn/courses/30/lessons/92342)

## 풀이에 관련된 주된 이론

- DFS

## 풀이 방법 (생각의 Flow 방식으로 글 작성)

- 10점부터 점수를 내는 경우와 안내는 경우로 나누고 재귀적 호출
- 처음에 남은 화살의 개수를 체크 후 0개면 리턴, 아니면 분기
- 호출된 단계가 0점일 경우 화살 모두 소모

## 어려웠던 이유 (푸는데 어려웠다면 작성)

- 완전 탐색까지는 떠올렸으나 구현을 하기가 어려움
- 동점 처리에서 헤맴

## 개선 방안 (효율성 테스트 결과가 실패했거나 더 좋은 아이디어가 있을 경우 작성)

- 코딩하는 과정에서 함수 두개로 나누어 작성했는데 리팩토링이 필요