# Open runways.csv

import csv
import webbrowser


with open('runways.csv', 'r') as f:
    reader = csv.DictReader(f)
    runways = {}
    for row in reader:
        if row['airport_ident'] not in runways:
            runways[row['airport_ident']] = []
        runways[row['airport_ident']].append(row)
    
    # Filter out all airports with more than 1 runway
    filtered_runways = {}
    for r in runways:
        if len(runways[r]) == 1:
            filtered_runways[r] = runways[r]

    runways = filtered_runways
    
    # Filter out all runways with a width less than 100 feet or more than 300 feet
    filtered_runways = {}
    for r in runways:
        try:
            if int(runways[r][0]['width_ft']) >= 100 and int(runways[r][0]['width_ft']) <= 300:
                filtered_runways[r] = runways[r]
        except:
            pass

    runways = filtered_runways

    # Filter out all runways that are not asphalt
    # (disabled because first round of filtering did not leave match)
    # filtered_runways = {}
    # for r in runways:
    #     if runways[r][0]['surface'] == '' or 'asp' not in runways[r][0]['surface'].lower():
    #         filtered_runways[r] = runways[r]

    # runways = filtered_runways

    # Filter out all runways that are not labelled 01 or 19
    filtered_runways = {}
    for r in runways:
        if runways[r][0]['he_ident'] in ['01', '19']:
            filtered_runways[r] = runways[r]

    runways = filtered_runways

    # Filter out all runways that do not have coordinates
    filtered_runways = {}
    for r in runways:
        if runways[r][0]['he_latitude_deg'] != '' and runways[r][0]['he_longitude_deg'] != '':
            filtered_runways[r] = runways[r]

    runways = filtered_runways

    # Print the link to the google maps view of the coordinates of the runway with satellite view
    for r in runways:
        # print(f'https://www.google.com/maps/search/?api=1&basemap=satellite&query={runways[r][0]["he_latitude_deg"]},{runways[r][0]["he_longitude_deg"]}')
        # https://www.google.com/maps/@?api=1&map_action=map&center=47.5951518,-122.3316393&zoom=17&basemap=satellite
        link = f'https://www.google.com/maps/@?api=1&map_action=map&center={runways[r][0]["he_latitude_deg"]},{runways[r][0]["he_longitude_deg"]}&zoom=17&basemap=satellite'
        webbrowser.open(link)

    