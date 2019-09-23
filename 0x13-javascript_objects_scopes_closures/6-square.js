#!/usr/bin/node

const SquareF = require('./5-square');

module.exports = class Square extends SquareF {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      c = String(c);
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
