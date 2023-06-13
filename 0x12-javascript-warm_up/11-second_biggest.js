#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
  process.exit(1);
}

const arr = [];

for (let i = 2; i < process.argv.length; i++) {
  const num = parseInt(process.argv[i], 10);
  arr.push(num);
}

let largest = arr[0];

for (let i = 1; i < arr.length; i++) {
  if (arr[i] > largest) {
    largest = arr[i];
  }
}

const index = arr.indexOf(largest);
arr.splice(index, 1);

let second = arr[0];

for (let i = 1; i < arr.length; i++) {
  if (arr[i] > second) {
    second = arr[i];
  }
}
console.log(second);
