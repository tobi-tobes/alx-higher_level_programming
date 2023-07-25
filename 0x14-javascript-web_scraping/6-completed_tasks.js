#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const output = {};

request(url, (error, response, body) => {
  if (error) {
    throw error;
  }
  if (response.statusCode !== 200) {
    return;
  }
  const tasks = JSON.parse(body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      const key = tasks[i].userId;
      if (key in output) {
        output[key]++;
      } else {
        output[key] = 1;
      }
    }
  }
  console.log(output);
});
