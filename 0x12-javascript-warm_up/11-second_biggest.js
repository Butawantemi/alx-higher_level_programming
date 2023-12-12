#!/usr/bin/node

const process = require('process');
const Args = process.argv;

if (isNaN(Args[2]) || isNaN(Args[3])) {
  console.log('0');
} else {
  const arr = Args.map(Number);
  arr.slice(2, Args.length);
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
