#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
