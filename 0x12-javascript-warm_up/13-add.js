#!/usr/bin/node
function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return (a + b);
  }
}
