#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h]; 
    }
  }

  /**
   * @property {method} print - prints the rectangle using the character X
   * @returns void
   */

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  /**
   * @property {method} rotate - exchanges the width and the height of the rectangle
   * @returns void
   */

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
   * @property {method} double - multiples the width and the height of the rectangle by 2
   * @returns void
   */

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
