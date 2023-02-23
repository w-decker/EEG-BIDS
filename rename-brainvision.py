# Title: Renaming BrainVision (.vhdr) EEG files
# Author: Will Decker




import os
import pandas as pd
import os.path as op
import mne
from mne_bids.copyfiles import copyfile_brainvision



rawdata = " " # path to raw data
rename = " " # path to new BIDS filder located within raw data folder, or simply write new path 


# Get a list of all files in the examples_dir
files = os.listdir(rawdata)

# Loop over each file in the folder
for i, file in enumerate(files):
    # Only process files with the .vhdr extension
    if os.path.splitext(file)[1] == ".vhdr":
        # Split the file name into parts (based on naming scheme: eeg_<task>_<subj#>.vhdr)
        file_parts = file.split("_")
        # Keep the three digits at the end of the file name
        file_number = file_parts[-1].split(".")[0]
        # Rename the file
        original = op.join(rawdata, file)
        renamed = op.join(rename, 'sub-' + file_number + '_ses-001_task-wordlearning_run-001.vhdr') # naming scheme based on BIDS format
        copyfile_brainvision(original, renamed, verbose=True)

        # Check that MNE-Python can read in both, the original as well as the renamed
        # data (two files: their contents are the same apart from the name)
        raw = mne.io.read_raw_brainvision(original)
        raw_renamed = mne.io.read_raw_brainvision(renamed)



# References

# Pernet, C.R., Appelhoff, S., Gorgolewski, K.J. et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data 6, 103 (2019). https://doi.org/10.1038/s41597-019-0104-8