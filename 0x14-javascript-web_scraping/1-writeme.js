#!/usr/bin/node

// Import the mode
const fs = require('fs');

// The first arg is the file path
const file = process.argv[2];

// The second arg is the string to write
const content = process.argv[3];

// Write to file
fs.writeFile(file, content, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
