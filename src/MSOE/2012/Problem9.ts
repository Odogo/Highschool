import readline from 'node:readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter a Roman numeral: ', (numeral) => {
    let total = 0;

    const romanValues: { [key: string]: number } = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };

    for (let i = 0; i < numeral.length; i++) {
        const current = numeral[i];
        const next = numeral[i + 1];

        if (!romanValues.hasOwnProperty(current)) {
            console.log('Invalid Roman numeral');
            rl.close();
            return;
        }

        if (next && !romanValues.hasOwnProperty(next)) {
            console.log('Invalid Roman numeral');
            rl.close();
            return;
        }

        if (next && romanValues[current] < romanValues[next]) {
            total -= romanValues[current];
        } else {
            total += romanValues[current];
        }
    }

    console.log('Decimal value:', total);
    rl.close();
});
