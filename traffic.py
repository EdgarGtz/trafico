import config
import pandas as pd
import numpy as np 
import sqlite3
import googlemaps
from datetime import datetime

# Connect to data base.

conn = sqlite3.connect('congestion_vial.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Call Google's API.

gmaps = googlemaps.Client(key = config.api_key)


# Insert traffic data.

# AIM - Perseverancia

response = gmaps.distance_matrix(('25.637351, -100.377698'),('25.635789, -100.377615'),
                  departure_time = 'now')

route_name = 'AIM - Perseverancia'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# AIM - Valle Oriente

response = gmaps.distance_matrix(('25.650102, -100.328202'),('25.649805, -100.327422'),
                  departure_time = 'now')

route_name = 'AIM - Valle Oriente'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# CECVAC

response = gmaps.distance_matrix(('25.642059, -100.347938'),('25.639425, -100.340973'),
                  departure_time = 'now')

route_name = 'CECVAC'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Centro Educativo Himalaya

response = gmaps.distance_matrix(('25.653898, -100.411717'),('25.651531, -100.412536'),
                  departure_time = 'now')

route_name = 'Centro Educativo Himalaya'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Centro Educativo Nobel

response = gmaps.distance_matrix(('25.656693, -100.396883'),('25.657725, -100.396410'),
                  departure_time = 'now')

route_name = 'Centro Educativo Nobel'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Centro Escolar Gante

response = gmaps.distance_matrix(('25.660291, -100.402436'),('25.659182, -100.402945'),
                  departure_time = 'now')

route_name = 'Centro Escolar Gante'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Colegio Alfonsino de San Pedro

response = gmaps.distance_matrix(('25.661402, -100.402954'),('25.660998, -100.401660'),
                  departure_time = 'now')

route_name = 'Colegio Alfonsino de San Pedro'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Colegio Ingles

response = gmaps.distance_matrix(('25.636431, -100.337056'),('25.637737, -100.336597'),
                  departure_time = 'now')

route_name = 'Colegio Ingles'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Colegio Labastida

response = gmaps.distance_matrix(('25.650118, -100.371152'),('25.651414, -100.371184'),
                  departure_time = 'now')

route_name = 'Colegio Labastida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Colegio Lic. Jose Vasconcelos

response = gmaps.distance_matrix(('25.680581, -100.418988'),('25.680381	-100.417767'),
                  departure_time = 'now')

route_name = 'Colegio Lic. Jose Vasconcelos'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Colegio Montessori Sierra Madre

response = gmaps.distance_matrix(('25.661951, -100.404668'),('25.661140, -100.404204'),
                  departure_time = 'now')

route_name = 'Colegio Montessori Sierra Madre'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Escuela Guadalupe

response = gmaps.distance_matrix(('25.662389, -100.400570'),('25.662511, -100.400985'),
                  departure_time = 'now')

route_name = 'Escuela Guadalupe'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Anglia

response = gmaps.distance_matrix(('25.666021, -100.408148'),('25.666507, -100.407116'),
                  departure_time = 'now')

route_name = 'Instituto Anglia'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Brillamont

response = gmaps.distance_matrix(('25.663670, -100.409352'),('25.664049, -100.410433'),
                  departure_time = 'now')

route_name = 'Instituto Brillamont'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Franco Mexicano

response = gmaps.distance_matrix(('25.651393, -100.372763'),('25.650092, -100.372230'),
                  departure_time = 'now')

route_name = 'Instituto Franco Mexicano'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Irlandes de Monterrey

response = gmaps.distance_matrix(('25.647482, -100.339400'),('25.647926, -100.335797'),
                  departure_time = 'now')

route_name = 'Instituto Irlandes de Monterrey'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Mano Amiga La Cima

response = gmaps.distance_matrix(('25.687152, -100.414678'),('25.687686, -100.414879'),
                  departure_time = 'now')

route_name = 'Instituto Mano Amiga La Cima'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Mater

response = gmaps.distance_matrix(('25.643072, -100.361242'),('25.641368, -100.361780'),
                  departure_time = 'now')

route_name = 'Instituto Mater'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto San Roberto

response = gmaps.distance_matrix(('25.644814, -100.336548'),('25.645056, -100.338566'),
                  departure_time = 'now')

route_name = 'Instituto San Roberto'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Instituto Welfare

response = gmaps.distance_matrix(('25.670494, -100.389106'),('25.669872, -100.387794'),
                  departure_time = 'now')

route_name = 'Instituto Welfare'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Liceo Anglo Frances de Monterrey

response = gmaps.distance_matrix(('25.658004, -100.36794'),('25.657461, -100.366152'),
                  departure_time = 'now')

route_name = 'Liceo Anglo Frances de Monterrey'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Liceo de Monterrey - Campus Valle Oriente

response = gmaps.distance_matrix(('25.650617, -100.329481'),('25.651377, -100.329104'),
                  departure_time = 'now')

route_name = 'Liceo de Monterrey - Campus Valle Oriente'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Necali Centro Educativo

response = gmaps.distance_matrix(('25.639412, -100.340957'),('25.638876, -100.339623'),
                  departure_time = 'now')

route_name = 'Necali Centro Educativo'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Pan American School

response = gmaps.distance_matrix(('25.653087, -100.332001'),('25.652086, -100.331988'),
                  departure_time = 'now')

route_name = 'Pan American School'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Preparatoria UDEM

response = gmaps.distance_matrix(('25.655545, -100.422617'),('25.657115, -100.422818'),
                  departure_time = 'now')

route_name = 'Preparatoria UDEM'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Preparatoria Anahuac - Irlandes

response = gmaps.distance_matrix(('25.647482, -100.339400'),('25.647926, -100.335797'),
                  departure_time = 'now')

route_name = 'Preparatoria Anahuac - Irlandes'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# American School Foundation of Monterrey

response = gmaps.distance_matrix(('25.657870, -100.443881'),('25.657379, -100.445030'),
                  departure_time = 'now')

route_name = 'American School Foundation of Monterrey'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Preparatoria Tec - Campus Santa Catarina

response = gmaps.distance_matrix(('25.663767, -100.432657'),('25.664120, -100.430681'),
                  departure_time = 'now')

route_name = 'Preparatoria Tec - Campus Santa Catarina'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = (response['rows'][0]['elements'][0]['distance']['value'])
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 2)
velocity = np.round(((distance / 1000) / (duration_traffic / 60)), decimals = 2)
avg_delay = np.round(duration_traffic / (distance / 1000), decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))

conn.commit()
conn.close()