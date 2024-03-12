#!/usr/bin/node

const fs = require('fs');

if (process.argv.length >= 5) {
  const fileA = fs.readFileSync(process.argv[2], 'utf8');
  const fileB = fs.readFileSync(process.argv[3], 'utf8');
  const text = fileA + '\n' + fileB;
  fs.writeFileSync(process.argv[4], text, 'utf8');
}
