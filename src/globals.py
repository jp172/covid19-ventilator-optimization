
# Evaluation function

CAPACITY_SCALAR = 0.25
TARGET_SCORE = 1e4

# Bed update generation

TIMESTEP = 50
UPDATE_CASES = ["normal_to_corona", "corona_leaves_hosp"]
BED_UPDATE_PROB = 10

# Hospitals initialization

NUMBER_FREE_BEDS = 25
NUMBER_CORONA_BEDS = 5
NUMBER_FREE_CORONA_BEDS = 3
NUMBER_CORONA_PAT_IN_NORMAL_BED = 1
SEVERITY_FOR_CORONA_BED = 0.8

# Properties for request generation

NUMBER_PATIENTS = 10000
NUMBER_DAYS = 150
LAT_DELTA = 0.1
LON_DELTA = 0.1
NUMBER_INITALLY_INFECTED = 10
EXPONENTIAL_RATE = 0.15

# Vehicle Properties

MAX_VEHICLE_RANGE = 100

# Precomputing parameters
NBR_SEGMENTS = 200
