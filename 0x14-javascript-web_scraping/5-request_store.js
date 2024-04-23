#!/usr/bin/node
/*
 * This script sends a request to a URL
 * and saves the body of the response to a file
 */

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.log(`Usage: ./${process.argv[1]} <URL> <FILE_PATH>`);
  process.exit(1);
}

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (err, res) => {
  if (err) {
    console.error('Error:', err.message);
  }

  fs.writeFile(fileName, res.body, 'utf8', (err) => {
    if (err) {
      console.error('Error:', err.message);
    }
  });
});
