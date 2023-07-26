#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charId = '18/';
let count = 0;

request(url, (error, response, body) => {
  if (error) throw error;
  if (response.statusCode !== 200) return;
  const films = JSON.parse(body);
  const filmsList = films.results;
  for (let i = 0; i < filmsList.length; i++) {
    const actors = filmsList[i].characters;
    for (let j = 0; j < actors.length; j++) {
      if (actors[j].endsWith(charId)) { count ++; }
    }
  }
  console.log(count);
});
