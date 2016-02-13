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

def get_total_surface_area(reader_shp_file):
    totalsqm = 0.0 # total square meters of pavement.
    if reader_shp_file.fields[3][1] == 'AREA_SQM':
        for record in reader_shp_file.iterRecords():
            totalsqm += record[3]
    else:
        print(" 'AREA_SQM' field not found")
    print("there are",totalsqm,"square meters of pavement")
    return totalsqm


def kwh(watts,hours):
    return watts*hours/1000

def watts_per_day(totalsqm,pavement_coverage_pc=50,solar_panel_max_watts_sqm=180,solar_panel_expected_efficiency_pc=25):
    pavement_coverage = pavement_coverage_pc / 100
    solar_panel_meters = totalsqm * pavement_coverage
    solar_panel_efficiency = solar_panel_expected_efficiency_pc / 100
    potential_max_watts_generated = solar_panel_meters * solar_panel_max_watts
    expected_watts_generated = potential_max_watts_generated * solar_panel_efficiency
    print(expected_watts_generated," watts out of a possible ",potential_max_watts_generated," watts")
    print("which is",kwh(expected_watts_generated,24),"an expected kilowatt hours per day, out of a possible", kwh(potential_max_watts_generated,24),"if ",pavement_coverage_pc, " of the pavement was covered in solar panels")

def cash_per_day_pounds(feed_in_pence_per_kilowatt,expected_watts_generated,potential_max_watts_generated):
    cash_per_day_expected = feed_in_pence_per_kilowatt * kwh(expected_watts_generated,24)/100
    cash_per_day_max = feed_in_pence_per_kilowatt * kwh(potential_max_watts_generated,24)/100
    return {"expected":cash_per_day_expected,"max":cash_per_day_max}


    print("which would be sold for £", cash_per_day_expected*24*365 ,"out of a potential £",cash_per_day_max*24*365,"per year")
