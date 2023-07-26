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
    if (tasks[i].completed === true) {
      const key = tasks[i].userId;
      if (key in output) {
        output[key]++;
      } else {
        output[key] = 1;
      }
    }
  }

  const length = Object.keys(output).length;
  let i = 0;
  process.stdout.write('{');

  if (length === 0) {
    console.log('}');
  } else if (length < 8) {
    for (const key in output) {
      process.stdout.write(`'${key}': ${output[key]}`);
      if (i < length - 1) {
        process.stdout.write(', ');
      }
      i++;
    }
    console.log(' }');
  } else {
    for (const key in output) {
      if (i === 0) {
        process.stdout.write(' ');
      } else {
        process.stdout.write('  ');
      }
      process.stdout.write(`'${key}': ${output[key]}`);
      if (i < length - 1) {
        process.stdout.write(',\n');
      }
      i++;
    }
    console.log(' }');
  }
});
