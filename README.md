# AquiOptic
A simple wrapper for the python-seabreeze library that lets you control your Ocean Optics device with high level commands. 

## Prerequisites
A python environment with python-seabreeze installed. 

## Getting Started
You can create a new conda environment with python through the anaconda prompt using the following commands: 
```
conda create --name <ENVIRONMENT NAME> conda
conda activate <ENVIRONMENT NAME>
conda install -c conda-forge python-seabreeze 
seabreeze_os_setup
conda env list
```

## Example Code
See exampleOptic.py for runnable examples

## Changelog
4/27/2021 python-seabreeze was recently updated to the newest version of python, so there is no need to downgrade your conda env to 3.6 anymore. 
