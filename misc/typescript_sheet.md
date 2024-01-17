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

Actually receiving input ***FROM*** the command line, however, is the tricky part.


# 4. Arithmetic Operations



# 5. Assignment Operations



# 6. Comments



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