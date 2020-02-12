#!/usr/bin/node
// Script that prints the title of Start Wars movie
const request = require('request');
const path = 'https://swapi.co/api/films/' + process.argv[2];
const ids = {};
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
          const val = JSON.parse(body).name;
          const key = JSON.parse(body).url.split('/')[5];
          ids[key] = val;
        }
        const lenIds = Object.getOwnPropertyNames(ids);
        if (lenIds.length === list.length) {
          for (const k in ids) {
            console.log(ids[k]);
          }
        }
      });
    });
  }
});
