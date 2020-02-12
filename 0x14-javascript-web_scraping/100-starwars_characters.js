#!/usr/bin/node
// Script that prints the title of Start Wars movie
const request = require('request');
const path = 'https://swapi.co/api/films/' + process.argv[2];
request(path, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const request1 = require('request');
    const list = JSON.parse(body).characters;
    list.forEach(elem => {
      request1(elem, function (error, response, body) {
        if (error) {
          console.log('error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
