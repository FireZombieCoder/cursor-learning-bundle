# Stage 0 Quiz: EVM Basics & Tooling

## Instructions
- Answer all questions to the best of your ability
- Each question is worth 1 point
- Total possible points: 8
- Passing score: 6/8 (75%)

---

## Question 1: Base Network
What is the Chain ID for Base-Sepolia testnet?

**A)** 8453
**B)** 84532
**C)** 1
**D)** 11155111

<details>
<summary>Click to reveal answer</summary>

**Answer: B) 84532**

Base-Sepolia testnet uses Chain ID 84532, while Base mainnet uses 8453.

</details>

---

## Question 2: EVM Storage
Which of the following is the most expensive in terms of gas cost?

**A)** Storage (SSTORE)
**B)** Memory (MSTORE)
**C)** Stack operations
**D)** Calldata

<details>
<summary>Click to reveal answer</summary>

**Answer: A) Storage (SSTORE)**

Storage operations are the most expensive, costing 20,000 gas for the first write and 5,000 gas for subsequent writes. Memory operations cost only 3 gas per word.

</details>

---

## Question 3: Foundry Tools
Which Foundry tool is used to perform RPC calls and interact with contracts?

**A)** Forge
**B)** Cast
**C)** Anvil
**D)** Chisel

<details>
<summary>Click to reveal answer</summary>

**Answer: B) Cast**

Cast is the Foundry tool for performing RPC calls, sending transactions, and interacting with contracts from the command line.

</details>

---

## Question 4: Solidity Functions
What is the difference between `view` and `pure` functions in Solidity?

**A)** `view` functions can modify state, `pure` functions cannot
**B)** `view` functions can read state, `pure` functions cannot
**C)** `pure` functions are more gas efficient
**D)** There is no difference

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `view` functions can read state, `pure` functions cannot**

- `view` functions can read state variables but cannot modify them
- `pure` functions cannot read or modify state variables
- Both are free to call (no gas cost when called externally)

</details>

---

## Question 5: Custom Errors
Why are custom errors preferred over `require` statements in modern Solidity?

**A)** They are more readable
**B)** They are more gas efficient
**C)** They provide better error messages
**D)** They are required by the compiler

<details>
<summary>Click to reveal answer</summary>

**Answer: B) They are more gas efficient**

Custom errors are more gas efficient because they don't store the error message as a string in the bytecode, unlike `require` statements.

</details>

---

## Question 6: Gas Optimization
Which of the following is NOT a gas optimization technique?

**A)** Using `immutable` for values set once
**B)** Packing structs to fit in storage slots
**C)** Using `calldata` instead of `memory` for function parameters
**D)** Using `public` variables instead of getter functions

<details>
<summary>Click to reveal answer</summary>

**Answer: D) Using `public` variables instead of getter functions**

Using `public` variables actually creates automatic getter functions, so there's no gas difference. The other options are all valid optimization techniques.

</details>

---

## Question 7: Python web3.py
What is the correct way to call a view function using web3.py?

**A)** `contract.functions.functionName().transact()`
**B)** `contract.functions.functionName().call()`
**C)** `contract.functions.functionName().send()`
**D)** `contract.functions.functionName().execute()`

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `contract.functions.functionName().call()`**

For view functions (read-only), use `.call()`. For state-changing functions, use `.transact()` or `.send()`.

</details>

---

## Question 8: Contract Deployment
What is the purpose of contract verification on block explorers?

**A)** To make the contract source code public
**B)** To reduce gas costs
**C)** To enable contract interaction through the explorer
**D)** Both A and C

<details>
<summary>Click to reveal answer</summary>

**Answer: D) Both A and C**

Contract verification makes the source code public and enables users to interact with the contract directly through the block explorer interface.

</details>

---

## Bonus Question: Gas Estimation
If a transaction costs 50,000 gas and the gas price is 20 gwei, what is the total cost in ETH?

**A)** 0.001 ETH
**B)** 0.0001 ETH
**C)** 0.00001 ETH
**D)** 0.000001 ETH

<details>
<summary>Click to reveal answer</summary>

**Answer: A) 0.001 ETH**

Calculation: 50,000 gas × 20 gwei = 1,000,000 gwei = 0.001 ETH
(1 ETH = 1,000,000,000 gwei)

</details>

---

## Scoring
- **8/8**: Excellent! You have a solid understanding of EVM basics and tooling.
- **6-7/8**: Good job! Review the missed concepts and you'll be ready for Stage 1.
- **4-5/8**: Not bad, but consider reviewing the lessons before proceeding.
- **0-3/8**: Please review the Stage 0 lessons thoroughly before moving on.

## Next Steps
Once you've completed this quiz with a passing score, you're ready to move on to Stage 1: Solidity Core concepts including types, memory/storage/calldata, and events.
