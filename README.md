# 🌹 Gilded Rose Kata 🌹

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

# Resources

These requirements and the initial state of the code are extracted from the original GitHub repository

[![Web](https://img.shields.io/badge/GitHub-emilybache-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main?tab=MIT-1-ov-file)

## Description

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city run by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in `Quality` as they approach their sell-by date.

We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, has moved on to new adventures. Your task is to add the new feature to our system so that
we can begin selling a new category of items. First an introduction to our system:

- All `items` have a `SellIn` value which denotes the number of days we have to sell the `items`
- All `items` have a `Quality` value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

Pretty simple, right? Well, this is where it gets interesting:

- Once the sell-by date has passed, `Quality` degrades twice as fast
- The `Quality` of an item is never negative
- __"Aged Brie"__ increases in `Quality` the older it gets
- The `Quality` of an item is never more than `50`
- __"Sulfuras"__, being a legendary item, never has to be sold or decreases in `Quality`
- __"Backstage passes"__, like aged brie, increases in `Quality` as its `SellIn` value approaches;
	- `Quality` increases by `2` when there are `10` days or less and by `3` when there are `5` days or less but
	- `Quality` drops to `0` after the concert

We have recently signed a supplier of conjured items. This requires an update to our system:

- __"Conjured"__ items degrade in `Quality` twice as fast as normal items

Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything
still works correctly. However, do not alter the `Item` class or `Items` property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the `UpdateQuality` method and `Items` property static if you like, we'll cover
for you).

Just for clarification, an item can never have its `Quality` increase above `50`, however __"Sulfuras"__ is a
legendary item and as such its `Quality` is `80` and it never alters.

## Objective

The main objective of this kata is:
 - Understand how good testing can help to refactor code
 - Identify code smells
 - Use IDE refactor tools to improve the code
 - Be able to refactor step by step the code so a new item can be added as easily as possible.

## Configuration

The project can be configured either by using `pip` or `pipenv`. Both ways will be explained.

<details><summary>Using pip</summary>

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment:
    ```bash
    source .venv/bin/activate # Linux / Mac
    .venv\Scripts\activate # Windows
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
</details>

<details><summary>Using pipenv</summary>

1. Install pipenv:
    ```bash
    pip install pipenv
    ```
2. Create a virtual environment with desire python version
    ```bash
    pipenv --python 3.11
    ```
   
    By default it will create the virtual environment outside the project. To create it inside the project, use the following command:
    ```bash
    PIPENV_VENV_IN_PROJECT=1 pipenv --python 3.11
    ```
3. Install the dependencies:
    ```bash
    pipenv install
    ```
</details>

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
pipenv run test
```

### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)