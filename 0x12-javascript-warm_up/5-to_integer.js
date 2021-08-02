#!/usr/bin/node
function toInt (num) {
  const integer = parseInt(num, 10);
  if (isNaN(integer)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + integer);
  }
}

if (process.argv.lenght === 2) {
  toInt('null');
} else {
  toInt(process.argv[2]);
}
