#!/usr/bin/node

const request = require('request');
const process = require('process');
const movie_id = process.argv[2];
const api_url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request.get(api_url, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else if (resp.statusCode !== 200) {
    console.log('code:', resp && resp.statusCode);
  } else {
    console.log(body.title);
  }
});
