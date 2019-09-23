#!/usr/bin/node
const dict = require('./101-data.js').dict;

const obj = {};

for (const key in dict) {
  const newKey = String(dict[key]);

  if (newKey in obj) {
    obj[newKey].push(key);
  } else {
    obj[newKey] = [];
    obj[newKey].push(key);
  }
}
console.log(obj);
