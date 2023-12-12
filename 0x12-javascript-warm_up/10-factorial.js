#!/usr/bin/node

const process = require('process');
const Args1 = process.argv[2];
const num = parseInt(Args1);

function calFactor (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * calFactor(x - 1);
  }
}

if (!isNaN(num)) {
  console.log(calFactor(num));
} else {
  console.log('1');
}
