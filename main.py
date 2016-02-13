import shapefile
# pyshp module

# https://pypi.python.org/pypi/geopy
from geopy.distance import vincenty


#gedisic
def measuredistance(longlat1,longlat2):
    return vincenty(longlat1,longlat2).meters

ba1Area = shapefile.Reader('/home/jason/Documents/GeoData/bath-pavement-data/Footways_BA1.shp')
bathOuter = shapefile.Reader('/home/jason/Documents/GeoData/bath-pavement-data/Footways_BathCityBoundary.shp')

print("ba1 has ",len(ba1Area.shapeRecords()),"walkways")
print("ba1 Outer has ",len(bathOuter.shapeRecords()),"walkways")

# for shape in ba1Area.iterShapeRecords():
#    pass

totalsqm = 0.0 #total square meters of pavement.

for record in ba1Area.iterRecords():
    totalsqm += record[3]

print("there are",totalsqm,"square meters of pavement in the ba1 inner area")

def kwh(watts,hours):
    return watts*hours/1000

pavement_coverage_pc = 50 #percent

pavement_coverage = pavement_coverage_pc / 100

solar_panel_meters = totalsqm * pavement_coverage

solar_panel_max_watts = 180 # per square meter

solar_panel_expected_efficiency_pc = 25 # 50 percent

solar_panel_efficiency = solar_panel_expected_efficiency_pc / 100

potential_max_watts_generated = solar_panel_meters * solar_panel_max_watts

expected_watts_generated = potential_max_watts_generated * solar_panel_efficiency

print("the ba1 inner area could generate ",expected_watts_generated," watts out of a possible ",potential_max_watts_generated," watts")
print("which is",kwh(expected_watts_generated,24),"an expected kilowatt hours per day, out of a possible", kwh(potential_max_watts_generated,24),"if ",pavement_coverage_pc, " of the pavement was covered in solar panels")

pence_per_kilowatt = 6.83 # feed in tarrif

cash_per_day_expected = pence_per_kilowatt * kwh(expected_watts_generated,24)/100

cash_per_day_max = pence_per_kilowatt * kwh(potential_max_watts_generated,24)/100


print("which would be sold for £", cash_per_day_expected*24*365 ,"out of a potential £",cash_per_day_max*24*365,"per year")
