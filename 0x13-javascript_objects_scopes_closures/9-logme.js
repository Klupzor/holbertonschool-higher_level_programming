#!/usr/bin/node
const arg = [];

exports.logMe = function (item) {
  arg.push(item);
  for (let i = 0; i < arg.length; i++) {
    console.log(i + ': ' + arg[i]);
  }
};
