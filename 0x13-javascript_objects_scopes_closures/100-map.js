#!/usr/bin/node

const list = require('./100-data.js').list;
let index = 0;
const newList = list.map(function (num) {
  const res = num * index;
  if (index < list.length) {
    index++;
  }
  return (res);
});

console.log(list);
console.log(newList);
