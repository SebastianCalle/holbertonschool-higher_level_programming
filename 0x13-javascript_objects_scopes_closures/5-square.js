#!/usr/bin/node
// Empty class Square
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
    constructor (size) {
          super(size, size);
        }
};
