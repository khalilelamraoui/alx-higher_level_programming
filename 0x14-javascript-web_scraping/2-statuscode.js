#!/usr/bin/node
/*
 * This script sends a request to a URL
 * and prints the status code
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log(`Usage: ./${process.argv[1]} <URL>`);
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
