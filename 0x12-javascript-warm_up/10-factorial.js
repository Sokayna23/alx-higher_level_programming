#!/usr/bin/node
const arg = process.argv[2];
const n = parseInt(arg);
function factorial (n) {
  if (n === 1 || n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(n));
