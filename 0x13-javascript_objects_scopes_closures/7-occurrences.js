#!/usr/bin/node
// Function that returns the number of occurrences

exports.nbOccurences = function (list, searchElement) {
  const subList = [];
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      subList.push(list[i]);
    }
  }
  return subList.length;
};
