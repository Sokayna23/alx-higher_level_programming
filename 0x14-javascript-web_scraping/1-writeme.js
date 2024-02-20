#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) { console.error(err); }
});
