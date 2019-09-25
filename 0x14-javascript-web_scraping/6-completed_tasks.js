#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const newDict = {};

request(url, (err, res, body) => {
  if (err) { console.log(err); } else {
    const todos = JSON.parse(body);
    todos.map((todo) => {
      if (todo.completed) {
        if (newDict[todo.userId]) { newDict[todo.userId]++; } else { newDict[todo.userId] = 1; }
      }
    });
    console.log(newDict);
  }
});
