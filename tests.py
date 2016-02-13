import shapefile

ba1Area = shapefile.Reader('/home/jason/Documents/GeoData/bath-pavement-data/Footways_BA1.shp')
bathOuter = shapefile.Reader('/home/jason/Documents/GeoData/bath-pavement-data/Footways_BathCityBoundary.shp')

print(ba1Area.fields[3])
print(bathOuter.fields[3])