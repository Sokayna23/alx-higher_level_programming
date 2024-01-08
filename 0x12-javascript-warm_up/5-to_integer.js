#!/usr/bin/node
const arg = process.argv[2];
const intNum = parseInt(arg);
if (!isNaN(intNum)) {
  console.log(`My number: ${intNum}`);
} else {
  console.log('Not a number');
}
