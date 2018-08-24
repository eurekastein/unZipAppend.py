# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:21:47 2018

@author: eureka
"""

import errno
import os
import shutil
import zipfile

TARGETDIR = '/media/eureka/eurekastein'
doc = r"/media/eureka/eurekastein/SCINCE2010/SCINCE20102.zip"

with open(doc, "rb") as zipsrc:
    zfile = zipfile.ZipFile(zipsrc)
    for member in zfile.infolist():
       target_path = os.path.join(TARGETDIR, member.filename)
       if target_path.endswith('/'):  # folder entry, create
           try:
               os.makedirs(target_path)
           except (OSError, IOError) as err:
               # Windows may complain if the folders already exist
               if err.errno != errno.EEXIST:
                   raise
           continue
       with open(target_path, 'wb') as outfile, zfile.open(member) as infile:
           shutil.copyfileobj(infile, outfile)