import readline from 'node:readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Start of the interval (a): ", (sA) => {
    const a = parseInt(sA);
    rl.question("End of the interval (b): ", (sB) => {
        const b = parseInt(sB);
        rl.question("Panels (n): ", (sN) => {
            const n = parseInt(sN);

            const h = (b - a) / n;
            let sum = 0.5 * (f(a) + f(b));
            for (let i = 1; i < n; i++) {
                sum += f(a + i * h);
            }
            
            console.log("Result: " + (h * sum));
            rl.close();
        });
    });
});

const f = (x: number) => Math.pow(x, 2);