#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
    for (let i = 2; i < process.argv.length; i++) {
      if (process.argv[i] > process.argv[i + 1]) {
        const max = process.argv[i];
	const maxindex = i;
      }
    }
    for (let i = 2; i < process.argv.length; i++) {
      if (process.argv[i] > process.argv[i + 1] && i !== maxindex) {
        const max2 = process.argv[i]; 
      }
    }
    console.log(max2);
  }

