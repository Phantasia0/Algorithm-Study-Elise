function solution(s) {
  let opened = 0;

  for (const char of s) {
    if (char == "(") opened++;
    else if (opened === 0) return false;
    else opened--;
  }

  return opened === 0;
}
