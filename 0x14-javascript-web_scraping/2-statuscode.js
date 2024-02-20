#!/usr/bin/node

const request = require('request');

const process = require('process');

url = process.argv[2];

request.get(url, (err, resp) => {
  if (err) {
    console.error(err)
  } else {
      console.log("code:", resp && resp.statusCode);
  }
});
