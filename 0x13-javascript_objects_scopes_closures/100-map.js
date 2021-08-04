#!/usr/bin/node
const alist = require('./100-data');
const result = alist.list.map(x => x * alist.list.indexOf(x));
console.log(alist.list);
console.log(result);
