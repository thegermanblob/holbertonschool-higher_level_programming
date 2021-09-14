#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
