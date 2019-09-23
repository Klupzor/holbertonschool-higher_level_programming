#!/usr/bin/node

exports.converter = function (base) {
  return function toBase (num) {
    return (num.toString(base));
  };
};
