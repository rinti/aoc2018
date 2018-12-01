import * as fs from 'fs'

const contents = fs.readFileSync('input.txt', {encoding: 'utf8'})

console.log(
    contents.split('\n').reduce((a, b) => +a + +b, 0)
)
