#!/usr/bin/node
// Script that concats 2 files
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const data1 = fs.readFileSync(fileA, 'utf-8');
const data2 = fs.readFileSync(fileB, 'utf-8');
fs.writeFile(fileC, data1 + data2, function (err) {
  if (err) {
    return console.log(err);
  }
});
