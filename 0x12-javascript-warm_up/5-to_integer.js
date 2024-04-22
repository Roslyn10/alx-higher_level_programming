#!/usr/bin/node
if (process.argv[2] !== undefined) {
  const argAsInt = parseInt(process.argv[2]);
  if (!isNaN(argAsInt)) {
    console.log('My number:', argAsInt);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
