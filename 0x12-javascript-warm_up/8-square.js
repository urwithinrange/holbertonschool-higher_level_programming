#!/usr/bin/node
const sym = 'X';
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log("Missing size");
} else {
    for (let i = 0; i < num; i++) {
      console.log(sym.repeat(num));
    }
}
