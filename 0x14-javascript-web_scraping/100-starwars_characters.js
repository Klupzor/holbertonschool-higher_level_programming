#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = 'http://swapi.co/api/films/' + args[2];

request(url, (err, response, body) => {
  if (err) { console.error('error:', err); } else {
    const characters = JSON.parse(body).characters;
    characters.map((character) => {
      request(character, (err, response, body) => {
        if (err) { console.error(err); } else { console.log(JSON.parse(body).name); }
      });
    });
  }
});
