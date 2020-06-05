# AquiOptic
A simple wrapper for the python-seabreeze library that lets you control your Ocean Optics device with high level commands. 

## Prerequisites
A python environment with python-seabreeze installed

## Getting Started
You can create a new conda environment with python 3.6 through the anaconda prompt using the commands: 
```
conda create --name <ENVIRONMENT NAME> python=3.6 conda
conda activate <ENVIRONMENT NAME>
conda install -c poehlmann python-seabreeze 
conda env list
```

## Example Code
Import the functions:
```
from AquiOptic import AquiOptic, AquiOptics
```
Define a new set of Ocean Optics Devices
```
myOptics = AquiOptics()
```
Print the device and serial number of all Ocean Optics devices
```
myOptics.printDevices()
```

Define a new AquiOptic with the serial number of the device
```
myOptic = AquiOptic("USB4H08370")
```

Return a list of the wavelengths:
```
print(myOptic.getWavelengths())
```
Return a corresponding list of intensities:
```
print(myOptic.getIntensities())
```

Returns a dict['wavelengths', 'intensities'] This re-calls the getWavelength and getIntensity functions.
```
mySpectra = myOptic.getSpectra()
print(mySpectra)
```

Creates the required directories which hold calibration files and spectras
```
myOptic.createSpectraFolders()
```

Save a spectra to the specified file name and path. If no path is specified, the default is ./Spectras
```
myOptic.saveSpectra(mySpectra, "mySpectra") 
```

Load a spectra from a file path. If no path is specified, the default is ./Spectras
```
loadedSpectra = myOptic.loadSpectra("mySpectra")
```

This variable holds a predefined calibration file that is loaded on creation of myOptic:
```
CalibrationSpectra = myOptic.Cal1
```

Overwrite a calibration spectra
```
myOptic.saveSpectra(CalibrationSpectra, myOptic.calibrationpath + "Cal1")
```

The newly updated Cal1 file can be accessed through this variable:
```	
myOptic.Cal1
```