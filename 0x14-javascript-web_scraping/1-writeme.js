#!/usr/bin/node

const fs = require('fs');

const output = process.argv[3];

try {
    fs.writeFileSync(process.argv[2], output);
} catch(error) {
    console.dir(error);
}
