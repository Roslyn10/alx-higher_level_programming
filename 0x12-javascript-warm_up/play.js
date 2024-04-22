#!/usr/bin/node
function add (a, b) {
  if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
    const arg1 = parseInt(process.argv[2]);
    const arg2 = parseInt(process.argv[3]);
    if (!isNaN(arg1) && !isNaN(arg2)) {
      return arg1 + arg2;
    } else {
      console.log('NaN');
      return null;
    }
  } else {
    return NaN;
  }
}
console.log(add());
