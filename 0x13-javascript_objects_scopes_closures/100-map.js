#!/usr/bin/node
// Function that imports an array and computes a new array
const list = require('./100-data');
console.log(list['list']);
let array = [list.length];
for (let i = 0; i < list['list'].length; i++) {
  array[i] = list['list'][i] * i;
}
console.log(array);
