Golden Globes
=============

Dependencies
------------
Python 2.7
nltk

Running
-------
First run the following file to build the analysis database (This will take a couple minutes).
`python gglobes.py`

Then run
`python runner.py`
to see some results!

You can also play with the results in the command line.
```python
>>> from runner import Runner
>>> r = Runner.read()
>>> winners = r.winners()
>>> host = r.host()
...
```