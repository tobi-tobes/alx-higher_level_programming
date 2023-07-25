#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

request(url, (error, response, body) => {
  if (error) console.log(error);
  const film = JSON.parse(body);
  const characters = film.characters;

  for (let i = 0; i < characters.length; i++) {
    const charUrl = characters[i];
    request(charUrl, (error, response, body) => {
      if (error) throw error;
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
