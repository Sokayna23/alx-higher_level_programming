#!/usr/bin/node

const request = require('request');

const process = require('process');

const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else if (resp.statusCode !== 200) {
    console.error('code:', resp && resp.statusCode);
  } else {
    const filmsWithWedge = body.results.filter((film) =>
      film.characters.some((character) => character.match(/\/people\/18\//)));
    console.log(filmsWithWedge.length);
  }
});
