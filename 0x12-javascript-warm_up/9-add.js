#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
function add (num1, num2) {
  return (num1 + num2);
}
console.log(add(num1, num2));
