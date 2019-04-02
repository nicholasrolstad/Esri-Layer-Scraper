import urllib2

# parameters
name = ''                       # name of county, etc. for file name
main_url = ''                   # REST endpoint for layer, will look like 'http://gis.co.ym.mn.gov/arcgis/rest/services/YellowMedicine/YellowMedicine_DataLayers/MapServer/40'
min_value = 0                   # integer, lowest value of objectid
max_value = 999                 # integer, highest value of objectid (or rounded up to nearest 1000-1 e.g. round 6758 to 6999 NOT 7000)
object_id_name = 'OBJECTID'     # may be something like 'OBJECTID_1'


# function that builds list of intervals to comply with 1000 feature limit per call
def build_list(min_value, max_value):
    interval_list = []
    minimum = round(min_value, -3)
    minimum = minimum - 1000 if minimum > min_value else minimum
    minimum = 0 if minimum < 0 else minimum
    maximum = minimum + 999

    while maximum < (max_value + 1000):
        interval_list.append([int(minimum), int(maximum)])
        maximum += 1000
        minimum += 1000

    return interval_list


where_clauses = build_list(min_value, max_value)

count = 1
for clause in where_clauses:
    url='{}/query?where={}%20>=%20{}%20AND%20{}%20<={}%20&outFields=*&f=json'.format(main_url, object_id_name, clause[0], object_id_name, clause[1])
    print url
    page = urllib2.urlopen(url)
    content = page.read()
    with open('{}_parcels{}.json'.format(name, count), 'w') as file:
        file.write(content)
    count += 1