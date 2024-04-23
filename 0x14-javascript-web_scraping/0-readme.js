#!/usr/bin/node
/*
 * This script reads a file and prints its content
 */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
