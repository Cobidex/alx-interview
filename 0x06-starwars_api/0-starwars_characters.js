#!/usr/bin/node

function getName (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request.get(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const actor = JSON.parse(body);
    console.log(actor.name);
    getName(characters, ++index);
  });
}

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  const index = 0;
  getName(characters, index);
});
