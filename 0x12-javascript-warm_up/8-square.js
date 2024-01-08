#!/usr/bin/node
const arg = process.argv[2];
const str = 'X';
const num = parseInt(arg);
if (!isNaN(num)) {
  for (let j = 0; j < num; j++) {
    let row = '';
    for (let i = 0; i < num; i++) {
      row += str;
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
