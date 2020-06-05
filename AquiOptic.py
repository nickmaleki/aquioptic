import seabreeze.spectrometers as sb
import os
import errno
import csv


# devices = sb.list_devices()
# print(devices)
# spec = sb.Spectrometer(devices[0])
# spec.integration_time_micros(12000)
# spec.wavelengths()

class AquiOptics:
    def __init__(self):
        self.devices = sb.list_devices()

    def setDevices(self):
        self.devices = sb.list_devices()

    def getDevices(self):
        return self.devices

    def printDevices(self):
        print(self.devices)


class AquiOptic:
    def __init__(self, serialNum):
        self.serialNum = serialNum
        self.device = sb.Spectrometer.from_serial_number(self.serialNum)
        self.integrationtime = 10000
        self.device.integration_time_micros(self.integrationtime)
        self.calibrationpath = "./Calibration Files/"
        self.spectrapath = "./Spectras/"
        self.CalDark = None
        self.Cal1 = None
        self.Cal2 = None
        self.Cal3 = None
        self.Cal4 = None
        # self.loadCalibrations()

    def open(self):
        self.device._open_device(self.device)

    def close(self):
        self.device.close()

    def setIntegrationTime(self, integrationtime):
        self.integrationtime = integrationtime
        self.device.integration_time_micros(self.integrationtime)

    def getWavelengths(self):
        return self.device.wavelengths()

    def getIntensities(self):
        return self.device.intensities()

    def createFolder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def createSpectraFolders(self):
        self.createFolder(self.calibrationpath)
        self.createFolder(self.spectrapath)

    def getSpectra(self):
        return {'wavelengths': self.getWavelengths(), 'intensities': self.getIntensities()}

    def loadSpectra(self, filepath):  # Defaults to loading from "Spectras" folder
        if ".csv" not in filepath:
            filepath += ".csv"
        if self.calibrationpath not in filepath and self.spectrapath not in filepath:
            filepath = self.spectrapath + filepath

        wavelengths = []
        intensities = []
        with open(filepath, 'r') as input:
            reader = csv.reader(input)
            for row in reader:
                wavelengths.append(row[0])
                intensities.append(row[1])

        spectra = {'wavelengths': wavelengths, 'intensities': intensities}
        return spectra

    def saveSpectra(self, spectra, filepath):
        if ".csv" not in filepath:
            filepath += ".csv"
        if self.calibrationpath not in filepath and self.spectrapath not in filepath:
            filepath = self.spectrapath + filepath

        res = zip(spectra['wavelengths'], spectra['intensities'])
        with open(filepath, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for line in res:
                writer.writerow([line[0], line[1]])

        if self.calibrationpath in filepath:
            self.loadCalibrations()

    def loadCalibrations(self):
        self.CalDark = self.loadSpectra(self.calibrationpath + "CalDark.csv")
        self.Cal1 = self.loadSpectra(self.calibrationpath + "Cal1.csv")
        self.Cal2 = self.loadSpectra(self.calibrationpath + "Cal2.csv")
        self.Cal3 = self.loadSpectra(self.calibrationpath + "Cal3.csv")
        self.Cal4 = self.loadSpectra(self.calibrationpath + "Cal4.csv")
