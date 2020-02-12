#!/usr/bin/node
// Script that prints the title of Start Wars movie
const request = require('request');
const path = 'https://swapi.co/api/films/' + process.argv[2];
request.get(path, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const list = JSON.parse(body).characters;
    list.forEach(elem => {
      request.get(elem, function (error, response, body) {
        if (error) {
          console.log('error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
