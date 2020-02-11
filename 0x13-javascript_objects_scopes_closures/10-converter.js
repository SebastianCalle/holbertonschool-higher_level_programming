#!/usr/bin/node
// Function that converts a nuber from base 10 to another base
exports.converter = function (base) {
  return function myConvert (num) {
    return num.toString(base);
  };
};
