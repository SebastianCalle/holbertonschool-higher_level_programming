#!/usr/bin/node
// Empty class Square
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c ===  undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let a = '';
      for (let j = 0; j < this.size; j++) {
        a += c;
      }
      console.log(a);
    }
  }
};
