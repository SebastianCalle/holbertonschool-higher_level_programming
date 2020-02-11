#!/usr/bin/node
// Script that displaya the status code of a GET request
const request = require('request');
const path = process.argv[2];
request(path, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
