#!/usr/bin/node
// script that print the addition of 2 inteers
const sum = function add (a, b) {
  return a + b;
};
console.log(sum(parseInt(process.argv[2]), parseInt(process.argv[3])));
