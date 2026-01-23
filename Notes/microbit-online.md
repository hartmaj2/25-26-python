# Running microbit online

- open [make_code](https://makecode.microbit.org/)
- New Project -> Code options -> Python only

## Watch out

- don't name your list `pins`
- types are named differently see [here](https://makecode.microbit.org/types)
- modulus function is weird `-1 % 5 = -1` instead of `-1 % 5 = 4` as in normal python
- if list is passed as untyped parameter to function, it cannot be looped through, you need to type it e.g. `def func(l : List[number])`

## Technical stuff

- GPIO pins cannot support a whole motor -> we need a transistor
- some GPIO pins can only function when the led display is off
- pins 19,20 cannot supply as much power as other pins

- [pin_information](https://makecode.microbit.org/device/pins)

## Python reference

- [makecode_docs](https://makecode.microbit.org/v2/python/)