function solution(chicken) {
  let answer = 0;
  let rest = 0;
  while(chicken/10 >= 1) {
      mod = parseInt(chicken/10) //10장당 쿠폰갯수
      answer += mod          //정답 누적
      rest = chicken % 10    //서비스사용x인 쿠폰
      chicken = mod + rest   //사용할수 있는 쿠폰
  }
  return answer;
}