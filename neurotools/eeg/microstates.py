"""
Microstates submodule.
"""
from .eeg import eeg_select_electrodes
from .miscellaneous import Time

import numpy as np
import pandas as pd
import mne


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def eeg_microstates_preprocess(epochs, subtract_column_mean_at_start=True, debug=True, use_gfp_peaks=True, force_avgref=True, use_smoothing=True, gfp_type_smoothing="DUPA"):
    """
    eeg : array
        Shape ntf*nch, conatains the EEG data the microstate modelmap analysis is to be computed on.
    """






