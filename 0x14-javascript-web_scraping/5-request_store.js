#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const output = body;
  try {
    fs.writeFileSync(filePath, output, 'utf-8');
  } catch (error) {
    console.dir(error);
  }
});
