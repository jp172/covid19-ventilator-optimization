import sqlite3
import inspect
from ..objects.hospital import Hospital
from ..objects.instance import Instance


def get_object_columns(my_object: object):
    attributes = inspect.getmembers(my_object, lambda a: not (inspect.isroutine(a)))
    object_columns = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
    return object_columns


def read_hospitals_from_db(request):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM hospitals')
    h = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
    c.connection.close()
    instance = Instance()
    instance.hospitals = h
    return instance


def get_hospital_from_database(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM hospitals WHERE id=?', id)
    h = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
    c.connection.close()
    return h[0]


def update_database_entry(request):

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    reported_hospital = Hospital()

    columns = get_object_columns(Hospital)
    query = "Insert INTO into hospitals (timestamp,{0}) values (?{1})"
    query = query.format(",".join(columns), ",?" * len(columns))

    reported_hospital = reported_hospital.to_dict()
    keys = tuple(reported_hospital[c] for c in columns)
    c.execute(query, keys)

    c.close()
