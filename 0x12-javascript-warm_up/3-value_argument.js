#!/usr/bin/node

// script that prints the first argument passed
const process = require('process');

const countArgs = process.argv;
if (countArgs[2]) {
  console.log(countArgs[2]);
} else {
  console.log('No argument');
}
