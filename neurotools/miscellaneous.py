# -*- coding: utf-8 -*-
import time as builtin_time
import pandas as pd

import os
import platform

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def read_data(filename, extension="", participant_id="", path="", localization="US"):
    """
    Load the datafile into a pandas' dataframe.

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pandas
    """
    # Find a corresponding file
    file = filename
    while os.path.isfile(file) is False:
        file = path + filename + extension
        file = path + participant_id + filename + extension
        if ".csv" in file:
            file = path + "/csv/" + participant_id + filename + extension
        elif ".xlsx" in file:
            file = path + "/excel/" + participant_id + filename + extension
        else:
            extension = ".xlsx"


    if localization == "FR" or localization == "FRA" or localization == "French" or localization == "France":
        sep = ";"
        decimal = ","
    else:
        sep = ","
        decimal = "."

    if ".csv" in file:
        try:
            df = pd.read_csv(filename, sep=sep, decimal=decimal, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(filename, sep=sep, decimal=decimal, encoding="cp1125")
    elif ".xls" in file or ".xlsx" in file:
        df = pd.read_excel(filename, encoding="utf-8")
    else:
        print("NEUROPSYDIA ERROR: read_data(): wrong extension of the datafile")
    return(df)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def save_data(df, filename="data", extension="all", participant_id="", path="", localization="US", index=False):
    """
    Save the datafile into a pandas' dataframe.

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pandas
    """
    if localization == "FR" or localization == "FRA" or localization == "French" or localization == "France":
        sep = ";"
        decimal = ","
    else:
        sep = ","
        decimal = "."

    if extension == "all":
        extension = [".csv", ".xlsx"]

    for ext in list(extension):
        if os.path.exists(path + "/csv/") is False:
            os.makedirs(path + "/csv/")
        df.to_csv(path + "/csv/" + participant_id + filename + ext, sep=sep, index=index, decimal=decimal, encoding="utf-8")
        if os.path.exists(path + "/excel/") is False:
            os.makedirs(path + "/excel/")
        df.to_csv(path + "/excel/" + participant_id + filename + ext, sep=sep, index=index, decimal=decimal, encoding="utf-8")

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
class Time():
    """
    A class object to get time.
    Its methods (functions) are:
        - reset()
        - get()
    See those for further informations.

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    >>> import neurotools as nt
    >>> myclock = nt.Time()
    >>> time_passed_since_myclock_creation = myclock.get()
    >>> myclock.reset()
    >>> time_passed_since_reset = myclock.get()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - time
    """
    def __init__(self):
        self.clock = builtin_time.clock()

    def reset(self):
        """
        Reset the clock of the Time object.

        Parameters
        ----------
        None

        Returns
        ----------
        None

        Example
        ----------
        >>> import neurotools as nt
        >>> time_passed_since_neuropsydia_loading = nt.time.get()
        >>> nt.time.reset()
        >>> time_passed_since_reset = nt.time.get()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - time
        """
        self.clock = builtin_time.clock()

    def get(self, reset=True):
        """
        Get time since last initialisation / reset.

        Parameters
        ----------
        reset = bool, optional
            Should the clock be reset after returning time?

        Returns
        ----------
        float
            Time passed in milliseconds.

        Example
        ----------
        >>> import neurotools as nt
        >>> time_passed_since_neurotools_loading = nt.time.get()
        >>> nt.time.reset()
        >>> time_passed_since_reset = nt.time.get()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - time
        """
        t = (builtin_time.clock()-self.clock)*1000

        if reset is True:
            self.reset()
        return(t)



# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def remove_following_duplicates(mylist):
    """
    Remove the duplicates that are following themselves, returning a list of ordered items.

    Parameters
    ----------
    mylist =  list
        A list

    Returns
    ----------
    The list without following duplicates.

    Example
    ----------
    >>> import neurotools as nt
    >>> mylist = ["a","a","b","a","a","a","c","c","b","b"]
    >>> nt.remove_following_duplicates(mylist)

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    None
    """
    mylist = mylist.copy()
    index = 0
    while index != len(mylist):
        try:
            while mylist[index] == mylist[index+1]:
                mylist.pop(index+1)
        except:
            pass
        index += 1
    return(mylist)

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def get_creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.

    Parameters
    ----------
    path_to_file =  str
        The path

    Returns
    ----------
    creation_date

    Example
    ----------
    >>> import neurotools as nt
    >>> date = nt.get_creation_date(path)

    Authors
    ----------
    Mark Amery

    Dependencies
    ----------
    - os
    - platform
    """
    if platform.system() == 'Windows':
        return(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            return(stat.st_birthtime)
        except AttributeError:
            print("Neuropsydia error: get_creation_date(): We're probably on Linux. No easy way to get creation dates here, so we'll settle for when its content was last modified.")
            return(stat.st_mtime)