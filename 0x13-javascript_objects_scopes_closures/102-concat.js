#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const data1 = fs.readFileSync(args[2]).toString();
const data2 = fs.readFileSync(args[3]).toString();
const data = data1 + data2;
fs.writeFile(args[4], data, (err) => {
  if (err) console.log(err);
});
