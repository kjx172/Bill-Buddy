# Bill Buddy

## Overview

This project is designed to manage and simplify transactions between members such as roomates or travellers. It is meant to help users keep track of who owes who what when dealing with group finances
## Features

- Add and remove members in the group
- Add transactions between members with specific reasons
- Search for transactions based on phrases and or member name
- Simplify the debt transactions using a max-flow algorithm

## Usage

### Graph Operations

1. **Add Member**: Adds a member to the graph.
2. **Remove Member**: Removes a member from the graph along with all their associated transactions.
3. **Add Transaction**: Adds a transaction between two members with a specified amount and reason.
4. **Search Transaction**: Searches for transactions based on a provided phrase.
5. **Simplify Debts**: Simplifies the debts by minimizing the number of transactions required to settle all debts.

### Simplification Algorithm

project inspiration and simplification algorithim come from [this medium article](https://medium.com/@mithunmk93/algorithm-behind-splitwises-debt-simplification-feature-8ac485e97688)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kjx172/Bill-Buddy.git
    cd Bill-Buddy
    ```

2. (Optional) Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. To run the Flask application, install Flask:
    ```bash
    pip install flask
    ```
