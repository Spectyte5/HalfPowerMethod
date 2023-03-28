# General Information

#### GUI web-based application for calculation of damping ratio for given system based on the half power method and created using django framework for python.

## Installation
To use the app you need to:
1. Clone repository using:
        git clone https://github.com/Spectyte5/HalfPowerMethod.git
2. Make sure you have all modules required (check requirements.txt)
3. Run Django server and enjoy the app.

## Pages
There are four different subpages:
1. Home - homepage with general information and links.
2. App - main section, used to input data and show result.
3. About - is the documentation you are viewing.
4. Contact - this section has information about the author.

## How to use it?
Data input has two parameters that correspond to transfer function from *scipy* module for python and should be passed in descending exponent order without brackets and seperated by spaces.
### Example:
-**Numerator:** 1 -3 which corresponds to s - 3

-**Denominator:**  1 0.4 1 which corresponds to s^2 + 0.4s + 1