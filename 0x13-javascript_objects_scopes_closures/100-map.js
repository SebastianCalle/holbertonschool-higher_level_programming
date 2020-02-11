#!/usr/bin/node
// Function that imports an array and computes a new array
const list = require('./100-data').list;
console.log(list)
let array = [];
array = list.map((x, i) => x * i);
console.log(array);
