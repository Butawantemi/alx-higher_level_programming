#!/usr/bin/node

const process = require('process');
const Args1 = process.argv[2];
const convertedArgs1 = parseInt(Args1);

if (!isNaN(convertedArgs1)) {
  console.log('My number:', convertedArgs1);
} else {
  console.log('Not a number');
}
