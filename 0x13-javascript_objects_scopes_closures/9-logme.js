#!/usr/bin/node
// FUnction that prints the number of arguments
let count = 0;
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count += 1;
};
