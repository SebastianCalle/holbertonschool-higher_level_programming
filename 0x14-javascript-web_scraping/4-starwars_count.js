#!/usr/bin/node
// Script that prints the title of Start Wars movie
const request = require('request');
const path = process.argv[2];
request(path, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const character = 'https://swapi.co/api/people/18/';
    const list = [];
    const dict = JSON.parse(body);
    for (const i in dict.results) {
      if (dict.results[i].characters.includes(character)) {
        list.push(i);
      }
    }
    console.log(list.length);
  }
});
