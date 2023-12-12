#!/usr/bin/node

const process = require('process');
const Args1 = parseInt(process.argv[2]);
const Args2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(Args2, Args1));
