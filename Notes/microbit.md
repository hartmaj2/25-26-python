# Notes on microbit

## IMPORTANT

- don't name your file `microbit.py` (it will then import itself instead of the module)

## Maintenance mode

Microbit can be put into maintenance mode by holding the reset button on the bottom side and while holding it connecting to the computer. Then releasing the button. The microbit will then show as MAINTENANCE folder mounted to my computer.

- [link1](https://microbit.org/get-started/user-guide/firmware/)

## Workflow

- install python module "uflash" using `pip install uflash`

- into my program import the `microbit` module

## Using the stubs

- for intelli sense to work I need to use so called stubs
- to get them, we can use `pip install microbit-stubs`

## Flashing the microbit

- to flash the program onto the microbit use `uflash <program_name>.py`

