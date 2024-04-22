#!/usr/bin/node

// Check if arguments are provided
if (process.argv.length === 2) {
  // No arguments provided
  console.log("undefined is undefined");
} else if (process.argv.length === 3) {
  // One argument provided
  const arg1 = process.argv[2];
  console.log(`${arg1} is undefined`);
} else if (process.argv.length === 4) {
  // Two arguments provided
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];
  console.log(`${arg1} is ${arg2}`);
} else {
  // More than two arguments provided
  console.log("Usage: node script.js <arg1> <arg2>");
  process.exit(1); // Exit with error code 1
}

