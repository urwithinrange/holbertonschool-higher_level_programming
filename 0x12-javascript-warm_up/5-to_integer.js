#!/usr/bin/node
const myArg = (process.argv[2]);
const myInt = parseInt(myArg);
if (typeof myInt === 'number' && !isNaN(myInt)) {
  console.log('My number:', myInt);
} else {
  console.log('Not a number');
}
