#!/usr/bin/node
// Script that gets content of a page an store in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(file, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
