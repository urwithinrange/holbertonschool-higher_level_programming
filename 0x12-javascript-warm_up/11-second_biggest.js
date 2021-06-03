#!/usr/bin/node
const num1 = process.argv;
if (num1.length < 4) {
  console.log(0);
} else {
  console.log(num1.sort().reverse()[1]);
}
