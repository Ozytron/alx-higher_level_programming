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
};
