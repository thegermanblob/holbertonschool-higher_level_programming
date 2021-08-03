#!usr/bin/node
module.exports = class Rectangle {
  constructor (h, w) {
    if (!isNaN(h) && !isNaN(w) && (h > 0 && w > 0)) {
      this.height = h;
      this.width = w;
    }
  }
};
