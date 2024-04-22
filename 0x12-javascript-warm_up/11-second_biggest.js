#!/usr/bin/node

if (process.argv.lenth < 4) {
  console.log('0');
  process.exit(1);
}

let largest = -Infinity;
let secondlargest = -Infinity;

for (let i = 2; i < process.argv.length; i++) {
  const num = parseInt(process.argv[i]);

  if (!isNaN(num)) {
    if (num > largest) {
      secondlargest = largest;
      largest = num;
    } else if (num > secondlargest && num !== largest) {
      secondlargest = num;
    }
  }
}
if (secondlargest === -Infinity) {
  console.log('0');
} else {
  console.log(secondlargest);
}
