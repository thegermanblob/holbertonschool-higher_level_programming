#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!isNaN(h) && !isNaN(w) && (h > 0 && w > 0)) {
      this.width = w;
      this.height = h;
    }
  }
};
