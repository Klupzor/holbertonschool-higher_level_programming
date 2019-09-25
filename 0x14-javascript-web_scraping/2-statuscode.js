#!/usr/bin/node
const args = process.argv;
const request = require('request');

request(args[2], function (error, response, body) {
  if (error) { console.log(error); }
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
