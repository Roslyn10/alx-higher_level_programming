#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let j = 0; j < this.height; j++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
