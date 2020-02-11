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
    let count = 0;
    let id = 1;
    for (let i = 1; i <= list.length - 1; i++) {
      if (id === list[i].userId && list[i].completed === true) {
        if (dict[id] === undefined) {
          dict[id] = 0;
        }
        count += 1;
        dict[id] = count;
      }
      if (list[i].userId > id) {
        id += 1;
        count = 0;
      }
    }
    console.log(dict);
  }
});
