import os
import time
import configparser
import pandas as pd
from glanvup.rizard import FloodProcess
from glanvup.cozard import CoastProcess
from glanvup.preprocess import WealthProcess
from glanvup.coverage import CoverageProcess
from glanvup.intersections import IntersectLayers
from glanvup.continents import south_coast
pd.options.mode.chained_assignment = None

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(__file__), 'script_config.ini'))
BASE_PATH = CONFIG['file_locations']['base_path']

DATA_RAW = os.path.join(BASE_PATH, 'raw')
DATA_PROCESSED = os.path.join(BASE_PATH, 'processed')
DATA_RESULTS = os.path.join(BASE_PATH, 'results')

path = os.path.join(DATA_RAW, 'countries.csv')
flood_folder = os.path.join(DATA_RAW, 'flood_hazard')
coastal_folder = os.path.join(DATA_RAW, 'coastal_hazard')

flood_files = os.listdir(flood_folder)
coast_files = os.listdir(coastal_folder)

countries = pd.read_csv(path, encoding = 'latin-1')
income_group = ['LIC', 'LMC', 'UMC']

'''for idx, country in countries.iterrows():

    if not country['income_group'] in income_group or country['gid_region'] == 0 or country['Exclude'] == 1:

        continue 
    
    for file in flood_files:

        try:
            flood_tiff = os.path.join(DATA_RAW, 'flood_hazard', file)

            #flooding = FloodProcess(path, countries['iso3'].loc[idx], flood_tiff)
            #flooding.process_flood_tiff()
            #flooding.process_flood_shapefile()

            #intersection = IntersectLayers(countries['iso3'].loc[idx], 'GSM', file)
            #intersection.pop_flood()
            #intersection.coverage_rizard()
            
            #intersection.vulri_intersect_all()
            #wealths = WealthProcess(path, countries['iso3'].loc[idx])
            #wealths.process_national_rwi()
            #wealths.process_regional_rwi()

            #coverages = CoverageProcess(path, countries['iso3'].loc[idx])
            #coverages.process_national_coverage()
            #coverages.process_regional_coverage()

            #intersection = IntersectLayers(countries['iso3'].loc[idx], 'GSM', file)
            #intersection.pop_flood()
            #intersection.pophaz_coverage()
            #intersection.intersect_all()

        except:

            pass'''
        
for coast in south_coast:

    for file in coast_files:

        try:

            coastal_tiff = os.path.join(DATA_RAW, 'coastal_hazard', file)

            coastal = CoastProcess(path, coast, coastal_tiff)
            coastal.process_flood_tiff() 
            coastal.process_flood_shapefile()

            intersection = IntersectLayers(coast, 'GSM', file)
            intersection.pop_cozard()
            intersection.coverage_cozard()
            #intersection.popcozard_coverage()
            #intersection.intersect_all_cozard()

        except:

            pass