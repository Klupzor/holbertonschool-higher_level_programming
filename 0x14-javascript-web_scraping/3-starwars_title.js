#!/usr/bin/node
const args = process.argv;
const request = require('request');

const url = 'http://swapi.co/api/films/' + args[2];

request(url, function (error, response, body) {
  if (error) { console.log(error); }
  console.log(JSON.parse(body).title);
});
