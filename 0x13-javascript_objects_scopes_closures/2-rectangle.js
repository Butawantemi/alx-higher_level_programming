#!/usr/bin/node

module.exports = class Rectangle {
  constr (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
