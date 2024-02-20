#!/usr/bin/node

const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, resp, body) => {
  if (error) {
    console.error(error);
  } else if (resp.statusCode !== 200) {
    console.error('code:', resp && resp.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
