#!/usr/bin/node
if (process.argv.length !== 3) {
  console.log('Missing number of occurrences');
  process.exit(1);
}

const x = parseInt(process.argv[2]);

for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
