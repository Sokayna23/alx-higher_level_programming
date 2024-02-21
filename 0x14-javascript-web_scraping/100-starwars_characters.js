#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, { json: true }, (error, response, movie) => {
  if (error) {
    console.error(`Error making API request: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
  } else {
    movie.characters.forEach((characterUrl) => {
      request.get(characterUrl, { json: true }, (charError, charResponse, character) => {
        if (charError) {
          console.error(`Error getting character: ${charError.message}`);
        } else if (charResponse.statusCode !== 200) {
          console.error(`Error: Received status code ${charResponse.statusCode}`);
        } else {
          console.log(character.name);
        }
      });
    });
  }
});
