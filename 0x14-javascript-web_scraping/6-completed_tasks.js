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
  let formattedOutput = "{ ";
  Object.keys(output).sort((a, b) => a - b).forEach(key => {
      formattedOutput += `  '${key}': ${output[key]},\n`;
  });
  formattedOutput = formattedOutput.slice(0, -2);
  formattedOutput += " }";
  
  formattedOutput = formattedOutput.replace(/\{(\s{2})/, "{");

  console.log(formattedOutput);
});
