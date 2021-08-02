#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let idx1 = 0; idx1 < process.argv[2]; idx1++) {
    let str = '';
    for (let idx2 = 0; idx2 < process.argv[2]; idx2++) {
      str += 'X';
    }
    console.log(str);
  }
}
