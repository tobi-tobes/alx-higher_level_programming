#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charId = '18';
let count = 0;
const searchStr = 'https://swapi-api.alx-tools.com/api/people/' + charId + '/';

request(url, (error, response, body) => {
  if (error) console.log(error);
  const films = JSON.parse(body);
  const filmsList = films.results;
  for (let i = 0; i < filmsList.length; i++) {
    const actors = filmsList[i].characters;
    if (actors.includes(searchStr)) {
      count++;
    }
  }
  console.log(count);
});
