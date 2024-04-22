#!/usr/bin/node

if (process.argv.length !== 3) {
  console.log('1');
  process.exit(1);
}

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('1');
  process.exit(1);
}

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const result = factorial(num);

console.log(result);
