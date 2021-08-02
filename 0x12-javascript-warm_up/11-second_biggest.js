#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
}
const array = process.argv;
array.shift();
array.shift();
const arrsorted = [...new Set(array)];
const arrsort = arrsorted.sort((a, b) => a - b);
console.log(arrsort[arrsort.length - 2]);
