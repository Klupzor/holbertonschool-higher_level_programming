#!/usr/bin/node

const SquareF = require('./5-square');

module.exports = class Square extends SquareF {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof c === 'string') {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
};
