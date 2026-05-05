# Dice Notation Generator for *Sophie's Dice* (incomplete)

Sophie's Dice and its documentation are made by Sophie Houlden, I'm just making this notation generator.

**IMPORTANT DISCLAIMER: This is not an official Sophie's Dice product.**

## Features

It supports the following features:
* Basic dice
* Value Replacement
* Everything in the [official documentation for dice expressions](https://sophiehoulden.com/dice/documentation/notation.html), except for:
    * Sub-expressions
    * Purely Cosmetic modifiers:
        * Redefine
        * Paint
        * Scale
    * Multi-results
    * Advanced dice generation with custom values
    * Sub-Expressions
    * Any math operator that isn't the 4 arithmetic operators or exponentiation
    * Variables and constants
    * User Values
    * Roll condition parameters

*WARNING: preset editing isn't supported yet, unless you know JSON and have a text editor*

## How to use
*`<PATH_TO_main.py>` represents where your `main.py` is*
1. Download the source code (whether it's via release or via the green `Code` button.)
2. Run the following commands:
    1. On Windows:
    ```cmd
    python <PATH_TO_main.py>
    ```
    Or if you're using the Python install manager instead of a standalone python version:
    ```cmd
    py <PATH_TO_main.py>
    ```
    2. On Unix systems (examples are MacOS or Linux):
    ```sh
    python3 <PATH_TO_main.py>
    ```
3. You should be prompted with 3 inputs: first one for the preset's file name, second one for the output's file name and third one for the amount of lines on the text file.

## Warnings

* Do not use an excessive tree depth nor an excessive line amount (nor both), it will eat your disk space!