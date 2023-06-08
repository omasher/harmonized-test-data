import csv
import logging
import random
import os

CURATION_STATUS = ['new', 'curated', ]

current_dir = os.getcwd()

# Change paths as necessary
hopitals_file = os.path.join(current_dir, 'hospitals.csv')
cities_file = os.path.join(current_dir, 'cities.csv')
names_file = os.path.join(current_dir, 'names.csv')

cities_list = []
first_names_list = []
last_names_list = []
institutions = []

institution_ids = []
physician_ids = []

def create_harmonized_institution():
    raise NotImplementedError("Implement")

def create_harmonized_physician():
    raise NotImplementedError("Implement")

def create_physician_x_institution():
    raise NotImplementedError("Implement")

with open(cities_file, newline='') as cities_csv:
    cities_reader = csv.reader(
        cities_csv, delimiter=',',)
    for idx, row in enumerate(cities_reader):
        if idx == 0:
            continue
        city, state = row
        cities_list.append(
            {'city': city, 'state': state})


with open(names_file) as names_csv:
    names_reader = csv.reader(
        names_csv)
    for idx, row in enumerate(names_reader):
        if idx == 0:
            continue
        first_name, last_name = row
        first_names_list.append(first_name)
        last_names_list.append(last_name)


def populate_institutions():
    logging.info(f"Creating institutions.....")
    with open(hopitals_file) as institutions_csv:
        hospitals_reader = csv.reader(
            institutions_csv)
        for row in hospitals_reader:
            institution = row[0]
            zip_code = f"{random.randrange(10000, 99999)}-{random.randrange(1000, 9999)}"
            city, state = random.choice(cities_list).values()
            curation = random.choice(CURATION_STATUS)
            institution_dict = {
                'institution_name': institution,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                'curated': curation
            }
            ids = create_harmonized_institution(**institution_dict)
            print(f"Institution id # {ids}")
            institution_ids.append(str(ids))


def populate_physicians():
    for _ in range(0, 10000):
        first_name = random.choice(first_names_list)
        last_name = random.choice(last_names_list)
        physician_dict = {
            'md_firstname_har': first_name,
            'md_lastname_har': last_name,
            'curated': 'curated',
        }
        md_phone = f"{random.randrange(100, 999)}-{random.randrange(100, 999)}-{random.randrange(1000, 9999)}"
        md_fax = f"{random.randrange(100, 999)}-{random.randrange(100, 999)}-{random.randrange(1000, 9999)}"
        md_email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
        ids = create_harmonized_physician(**physician_dict)
        print(f"Physician id # {ids}")
        physician_ids.append(
            {
                'harmonized_physician': str(ids),
                'md_phone': md_phone,
                'md_email': md_email,
                'md_fax': md_fax
            }
        )


def populate_physician_x_institution():
    for _ in range(0, 20000):
        harmonized_physician, md_phone, md_email, md_fax = random.choice(
            physician_ids).values()
        harmonized_institution = random.choice(institution_ids)
        pxi_dict = {
            'harmonized_physician': harmonized_physician,
            'harmonized_institution': harmonized_institution,
            'md_phone': md_phone,
            'md_email': md_email,
            'md_fax': md_fax,
            'curated': 'curated',
        }
        ids = create_physician_x_institution(**pxi_dict)
        print(f"Physician/Institution id # {ids}")
