import configparser
import os
import warnings
import pandas as pd
from glanvup.preprocess import ProcessCountry, ProcessRegions, ProcessPopulation 
pd.options.mode.chained_assignment = None
warnings.filterwarnings('ignore')

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(__file__), 'script_config.ini'))
BASE_PATH = CONFIG['file_locations']['base_path']

DATA_RAW = os.path.join(BASE_PATH, 'raw')
DATA_INTERMEDIATE = os.path.join(BASE_PATH, 'intermediate')
DATA_PROCESSED = os.path.join(BASE_PATH, 'processed')

path = os.path.join(DATA_RAW, 'countries.csv')
pop_tif_loc = os.path.join(DATA_RAW, 'WorldPop', 'ppp_2020_1km_Aggregated.tif')

country = ProcessCountry(path, 'USA')
national_outline = country.process_country_shapes()

regions = ProcessRegions('USA', 2)
regiona_shapefile = regions.process_regions()

populations = ProcessPopulation(path, 'USA', 2, pop_tif_loc)
country_pop = populations.process_national_population()
region_pop = populations.process_regional_population()