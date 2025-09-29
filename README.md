# dlpp-tutorials
Tutorials originally created for the Deep Learning in Particle Physics course, spring semester 2022, at the University of Heidelberg.
These tutorials were produced and delivered by Barry Dillon with the help of PhD students at the university:  Luigi Favaro, Theo Heimel, and Michel Luchmann.
They were modified in 2023 by Claudius Krause.

### Requirements

The python notebooks import various packages. You can install them using `pip`, preferably in a python virtual environment.

### Datasets

The physics datasets used for these tutorials were slightly too big to put here. They can be downloaded from the Heidelberg University website https://www.thphys.uni-heidelberg.de/~plehn/?visible=students, or via the script `data/get_data.py`

```bash
python data/get_data.py 1 data # amplitude regression (tuts 2,3,4)
python data/get_data.py 2 data # top tagging (tuts 5,6,7,8,9)
python data/get_data.py 3 data # anomaly detection (tut 10)
python data/get_data.py 4 data # event generation (tuts 11,12,13,14,15)
```

Alternatively, they can be downloaded from dropbox https://www.dropbox.com/s/n5e66w91rgmbqz2/dlpp-data.zip?dl=0
