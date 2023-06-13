#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
  process.exit(1);
}

for (let i = 0; i < size; i++) {
  let square = '';
  for (let j = 0; j < size; j++) {
    square = square + 'X';
  }
  console.log(square);
}
