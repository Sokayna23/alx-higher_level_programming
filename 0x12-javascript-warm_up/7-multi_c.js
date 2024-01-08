#!/usr/bin/node
const arg = process.argv[2];
let num = parseInt(arg);
if (!isNaN(num)) {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
} else {
  console.log('Missing number of occurrences');
}
