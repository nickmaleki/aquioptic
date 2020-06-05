# AquiOptic
A simple wrapper for the python-seabreeze library that lets you control your Ocean Optics device with high level commands. 

## Prerequisites
A python environment with python-seabreeze installed
If you are working with an Ocean Optics USB4000 You might need to install "windows-driver-files" for the drviers on the USB4000. 
You might be able to find more info [here](https://github.com/tbensky/labview_usb4000)

## Getting Started
You can create a new conda environment with python 3.6 through the anaconda prompt using the commands: 
```
conda create --name <ENVIRONMENT NAME> python=3.6 conda
conda activate <ENVIRONMENT NAME>
conda install -c poehlmann python-seabreeze 
conda env list
```

## Example Code
See exampleOptic.py for runnable examples