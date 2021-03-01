# Credit Card Number Generator and Validator

## Website: [CCGV](https://ccgv.herokuapp.com/)

## What is it?
CCGV is basic Flask web application for generating and validating credit card numbers.

## How it works?
- To generate or validate credit card number we need to check for some requirements.

    - first digits (individual for every brand)
    - length of the number (individual for every brand)
    - valid Luhn's algorithm

More about Luhn algorithm [here](https://www.geeksforgeeks.org/luhn-algorithm/)

## Specifications for available brands
 **Brand**            | **First Digits**     | **Length**               
 -------------------- | -------------------- | ---------------------
 American Express     | 34 or 37             | 15 digits            
 Master Card          | 50 - 55              | 16 digits            
 VISA                 | 4                    | 13, 16 or 19 digits                 