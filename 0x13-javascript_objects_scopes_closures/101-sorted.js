#!/usr/bin/node
// Script that imports a dictionary of occurrences
const dict = require('./101-data').dict;
const newDict = {};
for (const i in dict) {
  console.log(i);
  console.log(dict[i]);
  console.log(newDict[dict[i]]);
  if (newDict[dict[i]] === undefined) {
    newDict[dict[i]] = [];
  }
  newDict[dict[i]].push(i);
}
console.log(newDict);
