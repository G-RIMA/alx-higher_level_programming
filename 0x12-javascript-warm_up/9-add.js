#!/usr/bin/node
// prints the addition of two numbers
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
