#!/usr/bin/node

const fs = require('fs');
const file1 = fs.readFileSync(process.argv[2], 'utf-8');
const file2 = fs.readFileSync(process.argv[3], 'utf-8');
const output = file1 + file2;
fs.writeFileSync(process.argv[4], output);
