#!/usr/bin/node

const dict = require('./101-data.js').dict;
const arr = [];

for (const elem in dict) {
  if (!arr.includes(dict[elem])) {
    arr.push(dict[elem]);
  }
}

arr.sort();

const output = {};

for (let i = 0; i < arr.length; i++) {
  const temp = [];
  for (const elem in dict) {
    if (arr[i] === dict[elem]) {
      temp.push(elem);
    }
    output[arr[i]] = temp;
  }
}

console.log(output);
