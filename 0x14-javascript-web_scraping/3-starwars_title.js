#!/usr/bin/node

const request = require('request');
const process = require('process');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else if (resp.statusCode !== 200) {
    console.log('code:', resp && resp.statusCode);
  } else {
    console.log(body.title);
  }
});
