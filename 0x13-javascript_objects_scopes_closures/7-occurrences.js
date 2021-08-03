#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let result = 0;
  for (const item of list) {
    if (item === searchElement) {
      ++result;
    }
  }
  return result;
};
