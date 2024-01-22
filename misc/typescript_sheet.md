<h1>Handbook on Programming in Typescript</h1>

<h1>Table of Contents</h1>

- [1. Installation, Configuring, Executing](#1-installation-configuring-executing)
  - [1.1 Installing](#11-installing)
  - [1.2 Configuring](#12-configuring)
  - [1.3 Compling & Running](#13-compling--running)
- [2. Data Types](#2-data-types)
- [3. Console I/O](#3-console-io)
- [4. Arithmetic Operations](#4-arithmetic-operations)
- [5. Assignment Operations](#5-assignment-operations)
  - [5.1. Creating Variables](#51-creating-variables)
  - [5.2. Reassigning Variables](#52-reassigning-variables)
- [6. Comments](#6-comments)
- [7. Decision Structures](#7-decision-structures)
- [8. Conditional Operators](#8-conditional-operators)
- [9. Logic Operators](#9-logic-operators)
- [10. Advanced Decision Structures](#10-advanced-decision-structures)
- [11. String Methods](#11-string-methods)
- [12. Random Generation](#12-random-generation)
- [13. Looping Structures](#13-looping-structures)
- [14. Functions/Methods](#14-functionsmethods)
- [15. Elementary Data Structures](#15-elementary-data-structures)
  - [15.1 Arrays/Lists](#151-arrayslists)
  - [15.2 Matrices](#152-matrices)
- [References](#references)

# 1. Installation, Configuring, Executing

- [1.1 Installing](#11-installing)
- [1.2 Configuring](#12-configuring)
- [1.3 Compling & Running](#13-compling--running)

## 1.1. Installing
Before compling code, you need to install Typescipt.

1. Firstly, you need to install the latest LTS of [Node.js](https://nodejs.org), or the current branch, which can be found on the same link.
2. Node.js will have the package manager [NPM](https://www.npmjs.com) built-in, or additionally [Yarn](https://yarnpkg.com) can be used. From what I've seen, both work similar, but in this case, we will be using NPM for most actions.
3. After successfully installing Node.js (and checking if its already up-to-date, for whatever reason), execute the following command inside the root project folder.
```bash
npm install typescript @types/node
```
4. (Optional) Additionally, you may install an additional package to execute code without compiling it. This is useful in easy test cases. To install this package, execute:
```bash
npm install ts-node
```

> [!NOTE]
> You can install these globally by adding `-g` after `install`, such as
```bash
npm install -g typescript @types/node ts-node
```
## 1.2. Configuring
Before we can use Typescript, we have to tell it *how* we want to use it.

In the root directory of the project, create a file named `tsconfig.json`. If you don't know JSON syntax, you'll need to start the file with a set of `{}`.

Explaining how to configure Typescript will make this assignment into a fever dream, so enjoy [this resource](https://www.typescriptlang.org/tsconfig) which explains everything. But, since I'm nice, here's a nice template that I typically use in my projects:
```json
{
    "compilerOptions": {
        "lib": ["ESNext"],
        "module": "CommonJS",
        "moduleResolution": "Node",
        "target": "ESNext",
        "outDir": "dist",
        "sourceMap": false,
        "esModuleInterop": true,
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true,
        "allowSyntheticDefaultImports": true,
        "skipLibCheck": true,
        "skipDefaultLibCheck": true,
        "resolveJsonModule": true,
        "importHelpers": true,
        "strictNullChecks": true
    },

    "include": ["src"],
    "exclude": ["node_modules", "**/*.spec.ts"]
}
```
You can also find [this in the project tree](../tsconfig.json) of this repository, fancy that?

> [!WARNING]
> All code that is not sourced from the documentation is code that will be using the above `tsconfig.json`. Make sure to adapt the following code to your *own* settings, if you've made changed.

## 1.3. Compling & Running

Now that we have Typescript and it's related components installed, we may begin compiling code.

Creating Typescript files is simple. Create a new file with a `.ts` extension. Additionally, premade Javascript code with the extension `.js` may be able to be swapped to Typescript.

> [!CAUTION]
> Check your code after making the change from Javascript to Typescript files. A rewrite may need to take place if you wish to do such, but some errors may be able to be sorted out.

Compling Typescript files may be done by executing the following command into the terminal:
```bash
tsc
```
If you wish to learn more about this command, execute:
```bash
tsc -help
```

Now that we have our complied code, you'll notice wherever you tell Typescript to put your complied code, it's a bunch of Javascript files. **Congrats!** You found the entire purpose for Typescript, a statically-typed Javascript.

Executing the complied code is exactly how you would run normal Javascript code:
```bash
node <path>
```
An example, for reference:
```bash
node dist/src/index.js
```

> [!NOTE]
> If you have not installed the `ts-node` package, you may ignore the next section.

If you've installed the `ts-node` package mentioned earlier, you can execute Typescript code, which will compile and run for you (without leaving a trace of compiled code). You may do this by executing the following line:
```bash
ts-node <path-to-file>
```
An example in a [project of mine](https://github.com/Odogo/ShitpostBot), for reference:
```bash
ts-node src/index.ts
```

# 2. Data Types
Compared to Java's six (6) primitive types, Typescript only has three (3) primitive types:
- `string` - a string of characters, used as `"Hello world"`
- `number` - any number, everything is just a number, no `float`, `int`, `double`, etc.
- `boolean` - is.. what ya'd expect.

Compared to Java, a string is actually considered a primitive type now! Congrats, `string`, you have my appluase! :clap:

We'll talk more about additional data structures that Typescript offers, but, the more important item here.

### `any`
`any` is a fancy term for: "whatever the hell I want". It's great if you dont want stuff to be typechecked, but it's also a **massive pain in the ass.**

For example:
```typescript
let obj: any = { x: 0 };

obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;
```
These are all **LEGAL LINES OF CODE**, and it's disgusting. It's the exact reason why I switched from using Javascript to Typescript, is everything is typed.

In the `tsconfig.json`, you may imply `noImplicitAny`, which will flag any implicit `any` as an error. As the documentation states:
> When you don’t specify a type, and TypeScript can’t infer it from context, the compiler will typically default to any. You usually want to avoid this, though, because any isn’t type-checked. Use the compiler flag noImplicitAny to flag any implicit any as an error.

[Source: Typescript Documentation](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#noimplicitany)

# 3. Console I/O

There is no *readily* available Console I/O like how Java has it's `System.out` or `System.in`, but we do have the tools neccessary to do such without installing any additional packages.

Spitting out information to console is stupid simple:
```typescript
console.log("Hello world!");
```
Told ya.

Actually receiving input ***FROM*** the command line, however, is the tricky part. However it is possible to do such. Node[.js] has a nice set of built-in libraries almost like Java's packages. We can utilize one of these packages to create a reader to read console.

> [!NOTE]
> There are Streams for STDIN and STDOUT, you can use the `process` variable in every file to get those. `process.stdin` and `process.stdout`, but I find using this library handy, since we dont need to any additional libraries.

Firstly, at the top of our file, we need to add an import to be able to access the new stuff! At the top of your file, add one of these imports:
```typescript
// Uses functions inside of functions
// like 'object.function((arg) => {});'
import readline from 'node:readline';

// Uses promises
// like 'object.function().then((arg) => {});
import readline from 'node:readline/promises';
```
It's up to you how you want your code to be formatted. I personally like promises, but for small examples, function embedding will do the trick (and that's what we'll be doing for this handbook :wink:).

After we've added this import, we now need to create a `readline.Interface`, which is a class, and not an actual interface, relax.

To do so, we can do something like this:
```typescript
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
```

Great! Now we have a `readline.Interface`... how do we actually *use* it. **GREAT QUESTION, MATE**, something like this will do the trick:
```typescript
rl.question("Enter amount of layers: ", (sLayer) => {
    const layer = parseInt(sLayer);
    const total = (layer * (layer + 1) * (layer + 2 )) / 6;
    console.log("Total amount of balls: " + total);
    rl.close();
});
```
*This is an example from this repo, you can find the source code [here](../src/MSOE/2012/Problem4.ts).*

To break that code down, we executing a function on the `readline.Interface` to ask a question to the command line, in this case `"Enter amount of layers: `.

Our result is a `string` as `sLayer` inside of that arrow function. We want that as a number, so we execute `parseInt(sLayer)` to turn it into a number, an *integer* number.

Remember how I said earlier that there *are no* `int`, `float` or anything like that? Well, we can still parse items following the same intution behind integers, the nice thing is we can add decimals to that regardless of if it was parsed as an "int" or "float".

Back to the action, we do some fancy math, and now we have the total amount of balls in a ball pyramid with `x` layers.

# 4. Arithmetic Operations

Of course, any high level programming languages have your standard five (5):
- `+`, addition
- `-`, subtraction
- `*`, multiplication
- `/`, division
- `%`, modular (remainder in division)

We also have a static `Math` class, featuring your favourites:
- `Math.floor()`
- `Math.pow()`
- `Math.random()`
- `Math.min()` or `Math.max()`

Additionally, since Typescript is a demi-statically typed language (I say this because the `any` type exists), **type casting** exists.

Say we have a `Cow` class that extends an `Animal` class:
```typescript
class Animal {}
class Cow extends Animal {}
```
If we had...
```typescript
let cow: Cow = new Cow();
```
...we can cast that cow object into an animal like:
```typescript
let cow: Cow = new Cow();
let animal: Animal = (Animal)cow;
```

# 5. Assignment Operations

- [5.1. Creating Variables](#51-creating-variables)
- [5.2. Reassigning Variables](#52-reassigning-variables)

## 5.1. Creating Variables
There are mainly different ways to create variables, and some make it a lot easier to write code.

Here are some examples of creating variables:
```typescript
var a = 1;
let b = 2;
const c = 3;
```
### `var`
`var` was the original method to declare variables. There are a few problems with this, and why this is obsolete. Firstly, `var` has a problem, it doesn't like to be contained. Example being this:
```typescript
function f(shouldInitialize: boolean) {
  if (shouldInitialize) {
    var x = 10;
  }
  return x;
}
f(true); // returns '10'
f(false); // returns 'undefined'
```
I'm going to let the documentation explain:
> Some readers might do a double-take at this example. The variable `x` was declared within the `if` block, and yet we were able to access it from outside that block. That’s because `var` declarations are accessible anywhere within their containing function, module, namespace, or global scope - all which we’ll go over later on - regardless of the containing block. Some people call this **var-scoping** or **function-scoping**. Parameters are also function scoped.

*Source: [Typescript Docs - Variable Declaration](https://www.typescriptlang.org/docs/handbook/variable-declarations.html#scoping-rules)*

Which, is why we prefer...
### `let`
`let` is declared the exact same as `var` is. The documentation states the syntax is the same, but semantics are different. But, it's what you expect for most declarations.

Most declarations use **block-scoping**, which means a variable declared in a block i.e. `{ }`, stays in the block and doesn't bleed out.

For example, from [the documentation](https://www.typescriptlang.org/docs/handbook/variable-declarations.html#block-scoping)
> When a variable is declared using `let`, it uses what some call lexical-scoping or block-scoping. Unlike variables declared with `var` whose scopes leak out to their containing function, block-scoped variables are not visible outside of their nearest containing block or `for`-loop.
```typescript
function f(input: boolean) {
  let a = 100;
  if (input) {
    // Still okay to reference 'a'
    let b = a + 1;
    return b;
  }
  // Error: 'b' doesn't exist here
  return b;
}
```
> Here, we have two local variables `a` and `b`. `a`’s scope is limited to the body of `f` while `b`’s scope is limited to the containing `if` statement’s block.

### `const`
`const` is similar to `let`, except it cannot be changed once assigned. It's like adding a `final` to a field in Java.

Nothing further about `const`, it's literally a `let`. It's the same scoping rules and everything, but it cannot be changed once initialized.

## 5.2. Reassigning Variables

Reassigning variables is the same as initializing them. Declare the variable's name, then declare the object to set the variable as. Since Javascript is loose with their type declarations, we can do this:

```typescript
let variable = 0;
variable = 5;
variable = "hello";
variable = {
  type: "test",
  value: 1
}

// etc, etc.
```

**However**, since Typescript is designed to have statically-typed variables, if you have a variable like:
```typescript
let randomNumber: number = Math.random();
```
You cannot set the variable to a different type, an example:
```typescript
// ..using the variable declared above
randomNumber = 31; // valid
randomNumber = "hello!" // invalid
```

# 6. Comments

Declaring variables is similar to Java or Javascript.
```typescript
// Single line comments

/*
Multi-line comments
*/

/**
 * Documentation comments and declarations
 */
```

# 7. Decision Structures



# 8. Conditional Operators



# 9. Logic Operators



# 10. Advanced Decision Structures



# 11. String Methods



# 12. Random Generation



# 13. Looping Structures



# 14. Functions/Methods



# 15. Elementary Data Structures



## 15.1 Arrays/Lists



## 15.2 Matrices



# References

* [Markdown Cheatsheet](https://gist.github.com/jonschlinkert/5854601)
* [description](http://example.com)