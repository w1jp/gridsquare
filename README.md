# W1JP
Calculate gridsquare (Maidenhead Locator System) from a decimal lattitude and longitude.

This code is brute force written in python ≥ 3.6. Nothing elegant here. 

Type `python3 gridsqure.py -h` for help. 

For example my home is at 26.97611° N lattitude and 82.36151° W longitude. Note that West longitude is a negative longitude (West hemisphere) so:
`python3 gridsqure.py --lat 26.97611 --lng -82.36151`

This produces a gridsquare of: `EL86tx64`

For more information on MLS and gridsquares see [this introduction](http://www.arrl.org/grid-squares). 

Have fun,
Jon
