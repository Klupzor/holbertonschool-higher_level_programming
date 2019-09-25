#!/usr/bin/node
const request = require('request');
const args = process.argv;
const fs = require('fs');

request(args[2], (err, res, body) => {
  if (err) { console.log(err); } else {
    fs.writeFileSync(args[3], body, 'utf8', (err) => {
      if (err) { console.log(err); }
    });
  }
});
