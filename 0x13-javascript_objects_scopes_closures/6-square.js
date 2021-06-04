#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = c;
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
