import os, zipfile, fnmatch
from zipp import zipfile as zp
import geopandas as gpd

def extract_shps_to_gpkg(datPath = './', gpkgFile = 'example.gpkg'):
    
    for root, dirs, files in os.walk(datPath, topdown=True):
        for name in fnmatch.filter(files, '*.zip'):
          print(os.path.join(root, os.path.splitext(name)[0]))
          zp.ZipFile(os.path.join(root, name)).extractall(os.path.join(root, os.path.splitext(name)[0]))
    
    for root, dirs, files in os.walk(datPath, topdown=True):
      for name in fnmatch.filter(files, '*.shp'):
          print(os.path.join(root, name))
          fileName = os.path.splitext(name)[0]

          shpDat = gpd.read_file(os.path.join(root, name))
          shpDat.to_file(gpkgFile, driver='GPKG', layer=fileName)
