#!/usr/bin/node

const fs = require('fs').promises;
const path = require('path');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

const absolutePath = path.resolve(filePath);

async function readFileContent (file) {
  try {
    const content = await fs.readFile(file, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error('Error reading file:', error);
  }
}

readFileContent(absolutePath);
