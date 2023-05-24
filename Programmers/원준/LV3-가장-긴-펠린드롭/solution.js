function solution(s) {
  const validate = (word) => {
    const midIdx = Math.floor(word.length / 2);
    for (let i = 0; i < midIdx; i++) {
      if (word[i] !== word[word.length - i - 1]) {
        return false;
      }
    }

    return true;
  };

  for (let i = s.length; i >= 1; i--) {
    for (let j = 0; j <= s.length - i; j++) {
      const newWord = s.slice(j, i + j);
      if (validate(newWord)) {
        return newWord.length;
      }
    }
  }

  return 1;
}

const word = "abcdcba";

solution(word);
