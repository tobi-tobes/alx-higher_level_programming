#!/usr/bin/node

const fs = require('fs');

try {
    const file1 = fs.readFileSync(process.argv[2], 'utf-8');
    console.log(file1);
} catch(error) {
    console.dir(error);
}
