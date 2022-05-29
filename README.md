# Number printer 🧮 🖨
## Outline
Python script converts numbers (integers) into English words.

For example:
>2 -> two  
>900425 -> nine hundred thousand four hundred and twenty five  
>forty -> Please enter an integer between 0 and 1x10^18 - 1  
>0 -> zero

## Key Learnings:
* Writing out the logic / examples on paper first saves a lot of time and hair-pulling.
* Automated test input numbers (created in for loops) made it easier to identify bugs!
* English groups by ones (6), tens (60), hundreds (600), then thousands (6000), millions (6000000) etc. Thousands and higher orders are quantified by hundreds/tens/or ones. *e.g. 304000 = 'three hundred and four thousand'.* 
* Numbers of length 4 (6000) to length 6 (600000) are all classified as thousands, 7-9 are millions, 10-12 are billions etc.
* Important to consider where the *'and'* goes - it is used for hundreds and somethings, as well as anything that has a double digit at the end of it *('90 thousand and 99')*

## Try it for yourself!
1. Clone this repository on your machine
2. Run in your terminal inside the repo directory: ```python3 number_printer.py```
