from AquiOptic import AquiOptic, AquiOptics

myOptics = AquiOptics()  # Define a new set of Ocean Optics Devices
myOptics.printDevices()  # Print the device and serial number of all Ocean Optics devices

myOptic = AquiOptic("USB4H08370")

print(myOptic.getWavelengths())  # return a list of the wavelengths
print(myOptic.getIntensities())  # return a corresponding list of intensities

mySpectra = myOptic.getSpectra()
print(mySpectra)  # return dict['wavelengths', 'intensities'] This re-calls the getWavelength and getIntensity functions

myOptic.createSpectraFolders()  # creates the required directories which hold calibration files and spectras

myOptic.saveSpectra(mySpectra, "mySpectra")  # saves a spectra to the specified file name and path. If no path is specified, the default is ./Spectras

loadedSpectra = myOptic.loadSpectra("mySpectra")  # load a spectra from a file path. If no path is specified, the default is ./Spectras

CalibrationSpectra = myOptic.Cal1  # This variable holds a predefined calibration file that is loaded on creation of myOptic
myOptic.saveSpectra(CalibrationSpectra, myOptic.calibrationpath + "Cal1")  # overwrite a calibration spectra
myOptic.Cal1  # The newly updated Cal1 file can be accessed through this variable

