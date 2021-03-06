# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:59:28 2018

@author: eureka
"""

import os, subprocess
import errno
import shutil
import zipfile

TARGETDIR = '/media/eureka/eurekastein/SCINCE20102'
doc = r"/media/eureka/eurekastein/SCINCE20102.zip"

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

base_dir = r"/media/eureka/eurekastein/SCINCE20102"
names ={'municipal':'municipal.shp', 'estatal':'estatal.shp'}
for tabla, archivo in names.iteritems(): 
    full_dir = os.walk(base_dir)
    shapefile_list = []
    for source, dirs, files in full_dir:
        for file_ in files:
            if archivo in file_:
                shapefile_path = os.path.join(source, file_)
                shapefile_list.append(shapefile_path)
                
    count = 0            
    for shape_path in shapefile_list:
        if count == 0: 
            cmds = 'shp2pgsql -c -I -s 6362 -W LATIN1 ' + shape_path + ' ' + tabla + \
             ' | PGPASSWORD=postgres psql -h localhost -d db -U postgres'
        else:
            cmds = 'shp2pgsql -a -s 6362 -W LATIN1 ' + shape_path + ' ' + tabla + \
             ' | PGPASSWORD=postgres psql -h localhost -d db -U postgres'
        count +=1
        subprocess.call(cmds, shell=True)