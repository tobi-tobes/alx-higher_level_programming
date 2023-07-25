#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const output = {};

request(url, (error, response, body) => {
  if (error) console.log(error);
  const tasks = JSON.parse(body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      const key = (tasks[i].userId).toString();
      if (key in output) {
        output[key]++;
      } else {
        output[key] = 1;
      }
    }
  }
  console.log(output);
});
