#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (!C) {
      C = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += C;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
