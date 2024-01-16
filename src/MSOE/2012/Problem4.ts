import readline from 'node:readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter amount of layers: ", (sLayer) => {
    const layer = parseInt(sLayer);
    const total = (layer * (layer + 1) * (layer + 2 )) / 6;
    console.log("Total amount of balls: " + total);
    rl.close();
});