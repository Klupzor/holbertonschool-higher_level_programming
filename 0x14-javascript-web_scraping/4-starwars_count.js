#!/usr/bin/node
const args = process.argv;
const request = require('request');
let cont = 0;

const url = args[2];

request(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    const characters = JSON.parse(body).results.map((data) => data.characters);
    for (let i = 0; i < characters.length; i++) {
      cont = cont + characters[i].filter((x) => x.includes('18')).length;
    }

    console.log(cont);
  }
});
