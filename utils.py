import os
import dicom
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def load_data():

    cwd = os.getcwd()


    labels = pd.read_csv('stage1_labels.csv/stage1_labels.csv')

    labels = labels.as_matrix()

    ct = 0

    PathDicom = cwd + '/sample_images'
    lstFilesDCM = []  # create an empty list
    for dirName, subdirList, fileList in os.walk(PathDicom):
        pid = dirName[(len(dirName)-32):len(dirName)]
        print pid
        for filename in fileList:
            if ".dcm" in filename.lower():  # check whether the file's DICOM
                lstFilesDCM.append(os.path.join(dirName, filename))
                filename = filename[:(len(filename)-4)]
                for i in range(0,labels.shape[0]):
                    if pid == labels[i,0]:
                        print 'gotem: '+ str(ct)
                        ct = ct + 1



    num_images = len(lstFilesDCM)




    #being lazy, this will be fixed later on...


    xshape = 512
    yshape = 512

    image_data = np.ndarray([num_images, xshape, yshape])

    i = 0

    for dcmfile in lstFilesDCM:
        plan = dicom.read_file(dcmfile)

        image_data[i, :, :] = plan.pixel_array

        i = i + 1

    return image_data


x = load_data()

