#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  if (process.argv[2] > 0) {
    for (let idx = 0; idx < process.argv[2]; ++idx) {
      console.log('C is fun');
    }
  }
}
