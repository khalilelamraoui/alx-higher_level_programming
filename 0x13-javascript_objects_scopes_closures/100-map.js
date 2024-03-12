#!/usr/bin/node

const { list } = require('./100-data');
const mapedArr = list.map((x, idx) => x * idx);

console.log(list);
console.log(mapedArr);
