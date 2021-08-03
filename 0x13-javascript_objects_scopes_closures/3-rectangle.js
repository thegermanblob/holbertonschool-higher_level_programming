#!usr/bin/node
module.exports = class Rectangle {
  constructor (h, w) {
    if (!isNaN(h) && !isNaN(w) && (h > 0 && w > 0)) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let y = 0; y <= this.height; ++y) {
      let str = '';
      for (let x = 0; x <= this.height; ++x) {
        str += 'X';
      }
      console.log(str);
    }
  }
};
