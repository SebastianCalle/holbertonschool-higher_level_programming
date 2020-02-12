#!/usr/bin/node
// Script that prints the title of Start Wars movie
const request = require('request');
const path = process.argv[2];
request(path, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const list = JSON.parse(body).results;
    let count = 0;
    list.forEach(elem => {
      const characters = elem.characters;
      characters.forEach(item => {
        if (item.includes('/18')) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
