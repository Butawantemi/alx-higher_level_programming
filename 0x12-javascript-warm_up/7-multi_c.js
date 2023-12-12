#!/usr/bin/node

const process = require('process');
const Args1 = process.argv[2];

const x = parseInt(Args1);

if (!isNaN(x)) {
  for (let j = 0; j < x; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
