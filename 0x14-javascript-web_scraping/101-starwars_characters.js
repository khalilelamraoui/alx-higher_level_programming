#!/usr/bin/node
/*
 * This script sends a request to a URL
 * and prints the names of the characters
 * in the movie with the given ID
 */

const request = require('request');
const base = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length < 3) {
  console.error(`Usage: ./${process.argv[1]} <ID>`);
}

const movieUrl = `${base}films/${process.argv[2]}`;
request.get(movieUrl, async (err, res) => {
  if (err) {
    console.error('Error:', err.message);
  }

  const data = JSON.parse(res.body).characters;

  const ids = data.map((char) => {
    const id = (char.split('/'))[(char.split('/').length - 2)];
    return id;
  });

  for (const id of ids) {
    const charactersId = `${base}people/${id}`;
    await new Promise((resolve, reject) => {
      request.get(charactersId, (err, res) => {
        if (err) {
          console.error('Error:', err.message);
          reject(err);
        }
        console.log(JSON.parse(res.body).name);
        resolve();
      });
    });
  }
});
