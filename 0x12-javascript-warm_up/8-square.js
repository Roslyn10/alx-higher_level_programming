#!/usr/bin/node
if (process.argv.length !== 3) {
  console.log('Missing size');
  process.exit(1);
}

const size = parseInt(process.argv[2]);

if (isNaN(size)) { 
	console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
}
