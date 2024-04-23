#!/usr/bin/node
/*
 * This script sends a request to a URL
 * and prints the title of the Star Wars movie
 * with the given ID
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log(`Usage: ./${process.argv[1]} <ID>`);
  process.exit(1);
}

const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res) => {
  if (err) {
    console.error('Error: ', err.message);
    process.exit(1);
  }

  console.log(JSON.parse(res.body).title);
});
