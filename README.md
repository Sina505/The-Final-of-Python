# Python Mini Tools

A menu-based Python program with 8 small tools in one place: shapes, a calculator, a water bill splitter, and a few other things I wanted to practice. You pick a number from the menu and it takes you to that tool.

## The tools

| # | Tool | What it does |
|---|------|--------------|
| 1 | Shapes | Perimeter ("Environment") or area of a square, rectangle, circle or triangle |
| 2 | Calculator | `+` `-` `*` `/` `**`, log and square root |
| 3 | Water bill | Splits a water bill between 9 units using fixed shares and shows each amount in toman |
| 4 | Stars | Prints a triangle of stars with as many rows as you ask for |
| 5 | Factorial | Shows the factorial of a number step by step, like `1 * 2 * 3 = 6` |
| 6 | Multiplication table | Multiplies 1 to 10 by your number |
| 7 | Product list | You add products with a price and a quantity, and it prints a table with totals |
| 8 | Age | Calculates your age in years from your birth date |

## Running it

You only need Python 3, no extra libraries:

    python The_Finall.py

Type a number from 1 to 8 to open a tool. Type `end` to go back to the menu. Typing `end` in the menu closes the program.

## Things to know before using it

- **Type things exactly as shown.** The program is picky about spelling:
  - Shapes: `square`, `rectangle`, `circle`, `triangle` (all lowercase)
  - Shapes: `Environment` (that's the program's word for perimeter) or `Area`, with a capital first letter
  - Calculator: `log` in lowercase and `Radical` with a capital R
- **Whole numbers only.** All the number inputs expect integers, so something like `2.5` won't work.
- **Square and rectangle** ask for length, width and diameter (the diagonal). A square needs the same length and width, and a rectangle needs different ones. If the numbers don't match the shape, nothing is printed.
- **Triangle:** `Environment` asks for one side and multiplies it by 3, so it assumes all sides are equal. `Area` asks for the base and the height.
- **Square root** (`Radical`) uses the first number only. It still asks for a second one, but you can type anything.
- **Log** is calculated as the log of the first number with the second number as the base.
- **Product list:** the total price is price times quantity for every product you add.
- **Age tool:** enter your birth date as `year/month/day`, for example `2000/5/21`.
- If you enter something the program doesn't understand, it sends you back to the main menu without an error message.

## About this project

I wrote this as a final project to put together what I learned in Python: classes, loops, functions, lists and the `math` and `datetime` modules. The code is far from perfect, and there's a lot I'd clean up later, like better input checking and shorter code.