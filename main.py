from solve import solve

# this main file should just run a simulation given the following data.
# it should parse the following input specs nicely as arguments
hospital_data = "data/hospitals/hospitals.json"

request_data = "data/patient_requests/patients.json"

from schedulers.simple_scheduler import SimpleScheduler


# and of course other arguments, etc.
visualization = True
corona_takes_over_scenario = True


solve(hospital_data, request_data, SimpleScheduler())
