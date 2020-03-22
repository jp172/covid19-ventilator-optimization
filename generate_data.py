from src.data_generators.generate_patients import generate_patients
from src.data_generators.generate_requests import generate_requests
from src.data_generators.generate_hospitals import generate_hospitals

patients = generate_patients()
generate_requests(patients)
generate_hospitals()
