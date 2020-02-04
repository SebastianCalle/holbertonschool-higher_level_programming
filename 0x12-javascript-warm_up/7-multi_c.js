#!/usr/bin/node
// Script that prints x times "C is fun"
let i;
if (process.argv[2]) {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
