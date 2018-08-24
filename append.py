# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:17:17 2018

@author: eureka
"""

import os, subprocess

base_dir = r"/media/eureka/eurekastein/SCINCE2010"
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
    
    
