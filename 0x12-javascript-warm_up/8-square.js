#!/usr/bin/node
// script htat prints a square
const number = parseInt(process.argv[2]);
let x;
if (number) {
  for (let i = 0; i < number; i++) {
    x = '';
    for (let j = 0; j < number; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
