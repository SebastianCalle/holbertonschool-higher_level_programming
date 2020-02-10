#!/usr/bin/node
// Empty class Square
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c == undefined) {
      c = 'X'
      console.log(c);
    }
    for (let i = 0; i < this.width; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
};
