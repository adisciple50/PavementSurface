import shapefile

ba1Area = shapefile.Reader('~/Documents/GeoData/bath-pavement-data/Footways_Ba1.shp')
bathOuter = shapefile.Reader('~/Documents/GeoData/bath-pavement-data/Footways_BathCityBoundary.shp')

ba1Area.shapeRecords()