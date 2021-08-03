#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!isNaN(h) && !isNaN(w) && (h > 0 && w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; ++y) {
      for (let x = 0; x < this.width; ++x) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
};
