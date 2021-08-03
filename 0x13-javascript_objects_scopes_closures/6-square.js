#!/usr/bin/node
const Sqr = require('./5-square');
module.exports = class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.height; ++y) {
      for (let x = 0; x < this.width; ++x) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
