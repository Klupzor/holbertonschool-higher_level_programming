#!/usr/bin/node

const SquareF = require('./5-square');

module.exports = class Square extends SquareF {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      c = String(c);
      for (let i = 0; i < this.size; i++) {
        console.log(c[0].repeat(this.size));
      }
    } else {
      this.print();
    }
  }
};
