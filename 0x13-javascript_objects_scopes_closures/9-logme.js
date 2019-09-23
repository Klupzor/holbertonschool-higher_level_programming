#!/usr/bin/node
let cont = -1;

exports.logMe = function (item) {
  function print () {
    cont++;
    console.log(cont + ': ' + item);
  }

  print();
};
