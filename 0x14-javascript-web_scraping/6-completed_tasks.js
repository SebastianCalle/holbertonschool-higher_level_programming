#!/usr/bin/node
// Script that computes the number of task completed by user
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const list = JSON.parse(body);
    const dict = {};
    list.forEach(elem => {
      if (elem.completed === true) {
        if (dict[elem.userId] === undefined) {
          dict[elem.userId] = 1;
        } else {
          dict[elem.userId]++;
        }
      }
    });
    console.log(dict);
  }
});
