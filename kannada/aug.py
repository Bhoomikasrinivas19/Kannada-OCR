import os
import sys
from main import prediction_call


rootdir = ""
augdir = ""
enddir = ""

def augmentation(image_path,segdir):
    global rootdir, augdir
    from main import augmentation_call

    augdir = augmentation_call(image_path, segdir)
    imagelist = os.listdir(augdir)
    imagelist.sort()

augmentation('images/Processed/Segmented','images/Processed/Segmented/')