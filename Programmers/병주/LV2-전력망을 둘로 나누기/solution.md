# solution.md 가이드 폼

## 문제 이름과 링크

- [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)
- Level 2

## 풀이에 관련된 주된 이론

- 완전탐색

## 풀이 방법 (생각의 Flow 방식으로 글 작성)

- 전선을 순회하며 각각의 송전탑에 연결되어 있는 송전탑정보를 맵핑한다.
- 전선을 순회하며 송전탑정보로 연결고리를 확인한다. (시작과 끝은 방문한것으로 간주)

## 어려웠던 이유 (푸는데 어려웠다면 작성)

- 완전탐색 숙련도 미흡
- 송전탑의 연결고리에 따라 나누는 것에 대한 접근
- 멀쩡한 송전탑을 도대체 왜 짤라야 하는가?

## 개선 방안 (효율성 테스트 결과가 실패했거나 더 좋은 아이디어가 있을 경우 작성)
