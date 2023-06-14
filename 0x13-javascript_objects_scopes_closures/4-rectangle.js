#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const h = this.height;
    const w = this.width;
    for (let i = 0; i < h; i++) {
      let rect = '';
      for (let j = 0; j < w; j++) {
        rect = rect + 'X';
      }
      console.log(rect);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
