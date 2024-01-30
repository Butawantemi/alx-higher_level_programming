#!/usr/bin/node

// Import the module
const request = require('request');
const fs = require('fs');

// The first arg is the URL to request
const apiUrl = process.argv[2];

// The second arg the file path to store the body response
const file = process.argv[3];

// Make an HTTP GET request to the specified URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Write response to file
    fs.writeFile(file, body, 'utf-8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
