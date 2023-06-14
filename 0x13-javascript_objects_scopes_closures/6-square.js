#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  print () {
    super.print();
  }

  rotate () {
    super.rotate();
  }

  double () {
    super.double();
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const h = this.height;
      const w = this.width;
      for (let i = 0; i < h; i++) {
        let square = '';
        for (let j = 0; j < w; j++) {
          square += c;
        }
        console.log(square);
      }
    }
  }
};
