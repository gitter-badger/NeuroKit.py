

# <img src="https://github.com/neuropsychology/NeuroKit.py/blob/master/examples/files/icon.png" width="700" align="center" alt="neurokit python"> NeuroKit.py
A Python Toolbox for Statistics and Signal Processing (EEG, EDA, ECG, EMG...).



|Name|NeuroKit|
|----------------|---|
|Latest Version|[![](https://img.shields.io/badge/version-0.0.1-brightred.svg)](https://github.com/neuropsychology/NeuroKit.py)|
|Authors|[![](https://img.shields.io/badge/CV-D._Makowski-purple.svg?colorB=9C27B0)](https://cdn.rawgit.com/neuropsychology/Organization/master/CVs/DominiqueMakowski.pdf)|

---

**Warning: these functions might be, for now, NOT GENERALIZABLE to your data as I've intented them specifically for my personal use. However, with time, I'll try to open and expand them as much as I can.**

## Description

Features:

- EEG (wrapper functions based on [mne](http://martinos.org/mne/stable/index.html))
- EDA

## Install

Run the following:

```bash
pip install https://github.com/neuropsychology/NeuroKit.py/zipball/master
```

## Example

```python
import neurokit as nk
mylist = ["a","a","b","a","a","a","c","c","b","b"]
nk.remove_following_duplicates(mylist)
```
