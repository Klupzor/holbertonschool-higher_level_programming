#!/usr/bin/node

const SquareF = require('./5-square');

module.exports = class Square extends SquareF {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    c = String(c)
    if (c && c.length === 1) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
};
