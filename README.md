# NeuroTools
A Python Toolbox for Statistics and Signal Processing (EEG, EDA, ECG, EMG...).

|Name|NeuroTools|
|----------------|---|
|Latest Version|[![](https://img.shields.io/badge/version-0.0.1-brightred.svg)](https://github.com/neuropsychology/NeuroTools.py)|
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
pip install https://github.com/neuropsychology/NeuroTools.py/zipball/master
```

## Example

```python
import neurotools as nt
mylist = ["a","a","b","a","a","a","c","c","b","b"]
nt.remove_following_duplicates(mylist)
```
