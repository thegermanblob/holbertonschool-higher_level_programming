#!/usr/bin/node
let index = 0;
function thing () {
  let item;
  for (item of process.argv) {
    ++index;
    if (index === 3) { break; }
  }
  if (index === 2) {
    console.log('No argument');
  }
  if (index > 2) {
    console.log(item);
  }
}
thing();
