#!/usr/bin/node
// Script that print number
if (parseInt(process.argv[2])) {
  console.log('My number ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
