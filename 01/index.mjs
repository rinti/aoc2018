import * as fs from 'fs'

const contents = fs.readFileSync('input.txt', {encoding: 'utf8'})

// Part 1
console.log(
    contents.split('\n').reduce((a, b) => +a + +b, 0)
)

// Part 2

let freq = 0
let freqs = {}

const loopAndCheck = () => {
    contents.split('\n').forEach(i => {
        freq += +i

        if(freqs[freq] && +i !== 0) {
            console.log(freq)
            process.exit(1)
        }

        freqs[freq] = 1
    }) 
    loopAndCheck()
}

loopAndCheck()



