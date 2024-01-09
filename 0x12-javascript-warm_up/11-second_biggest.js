#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max = Number.MIN_SAFE_INTEGER;
  let max2 = Number.MIN_SAFE_INTEGER;
  for (let i = 2; i < process.argv.length; i++) {
    const currentNum = parseInt(process.argv[i]);
    if (currentNum > max) {
      max2 = max;
      max = currentNum;
    } else if (currentNum > max2 && currentNum < max) {
      max2 = currentNum;
    }
  }
  console.log(max2 === Number.MIN_SAFE_INTEGER ? 0 : max2);
}
