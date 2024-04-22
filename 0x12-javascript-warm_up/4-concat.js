#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('undefined is unefined');
} else if (process.argv.length === 3) {
  const arg1 = process.argv[2];
  console.log(`${arg1} is undefined`);
} else if (process.argv.length === 4) {
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];
  console.log(`${arg1} is ${arg2}`);
}
