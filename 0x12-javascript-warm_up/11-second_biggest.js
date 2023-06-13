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
let second = arr[0];

for (let i = 1; i < arr.length; i++) {
  if (arr[i] > largest) {
    if (largest > second) {
      second = largest;
    }
    largest = arr[i];
  }
}
console.log(second);
