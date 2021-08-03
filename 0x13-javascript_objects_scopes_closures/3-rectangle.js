#!usr/bin/nodeZ
module.exports = class Rectangle {
  constructor (w, h) {
    if (!isNaN(h) && !isNaN(w) && (h > 0 && w > 0)) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let y = 0; y < this.height; ++y) {
      let str = '';
      for (let x = 0; x < this.width; ++x) {
        process.stdout.write("X");
      }
      process.stdout.write("\n");
    }
  }
};
