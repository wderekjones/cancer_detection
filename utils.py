import numpy as np
import os
import dicom
import matplotlib.pyplot as plt


def load_data(path):
    plan = dicom.read_file('stage1/0/0_0.dcm')

    PathDicom = "./stage1/0/"
    lstFilesDCM = []  # create an empty list
    for dirName, subdirList, fileList in os.walk(PathDicom):
        for filename in fileList:
            if ".dcm" in filename.lower():  # check whether the file's DICOM
                lstFilesDCM.append(os.path.join(dirName, filename))

    num_images = len(lstFilesDCM)

    image = plan.pixel_array

    xshape, yshape = image.shape

    image_data = np.ndarray([num_images, xshape, yshape])

    i = 0

    for dcmfile in lstFilesDCM:
        plan = dicom.read_file(dcmfile)

        image_data[i, :, :] = plan.pixel_array

        i = i + 1

    return image_data