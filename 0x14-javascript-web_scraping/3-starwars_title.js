#!/usr/bin/node
// Script that prints the title of Start Wars movie
const request = require('request');
const id = process.argv[2];
const path = 'http://swapi.co/api/films/' + id;
request(path, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body)['title']);
  }
});
