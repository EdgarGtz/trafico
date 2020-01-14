import pandas as pd
import numpy as np
import sqlite3

# Connect to the data base.

conn = sqlite3.connect('congestion_vial.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Create the "routes" table.

cursor.execute('''CREATE TABLE routes
        (route_name text PRIMARY KEY, origin text, destination text) ''')

# Insert routes.

cursor.execute(''' INSERT INTO routes VALUES
        ("AIM - Perseverancia", "Perseverancia 111, Zona Colinas de La Sierra Madre, San Pedro Garza Garcia, N.L., Mexico",
        "Perseverancia 139, Zona Colinas de La Sierra Madre, 66280 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("AIM - Valle Oriente", "Humberto Junco Voigt 2307, Valle Oriente, 66290 San Pedro Garza Garcia, N.L., Mexico",
        "Humberto Junco Voigt 2311-S, Zona Loma Larga Oriente, Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("CECVAC", "Av Alfonso Reyes 102, San Patricio 2o Sector, 66270 San Pedro Garza Garcia, N.L., Mexico",
        "Av Alfonso Reyes 801-717, Zona San Agustin Campestre, San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Centro Educativo Himalaya", "Las Sendas 100, Zona Valle Poniente, San Pedro Garza Garcia, N.L., Mexico",
        "Las Sendas 100, Zona Valle Poniente, San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Centro Educativo Nobel", "5 de Mayo 1070, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Diego de Montemayor 1001-395, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Centro Escolar Gante", "Gral Vicente Guerrero 222-223, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Gral Vicente Guerrero, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Colegio Alfonsino de San Pedro", "Lazaro Garza Ayala 211, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Lazaro Garza Ayala 310-372, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Colegio Ingles", "Av. Real San Agustin, Zona Lomas de San Agustin, San Pedro Garza Garcia, N.L., Mexico",
        "Av. Eugenio Garza Laguera, Zona Lomas de San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Colegio Labastida", "Del Valle Sector Fatima, San Pedro Garza Garcia, Nuevo Leon, Mexico",
        "Rio Tigris, Del Valle Sector Fatima, San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Colegio Lic. Jose Vasconcelos", "2 de Noviembre 803, Fama V, 66116 Santa Catarina, N.L., Mexico",
        "Perseverancia 139, Zona Colinas de La Sierra Madre, 66280 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Colegio Montessori Sierra Madre", "Lazaro Garza Ayala 152, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Lic. Benito Juarez Sur 205-203, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Escuela Guadalupe", "Manuel Gonzalez, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Gral. Porfirio Diaz, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Anglia", "Calle Jimenez, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Calle Libertad 511-523, Casco Urbano, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Brillamont", "Lazaro Garza Ayala SN-C OXXO, Rincon de San Francisco, 66238 San Pedro Garza Garcia, N.L., Mexico",
        "Lazaro Garza Ayala, Rincon de San Francisco, 66238 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Franco Mexicano", "Eje Metropolitano 8 51-59, Del Valle Sector Fatima, San Pedro Garza Garcia, N.L., Mexico",
        "Rio Tiber Poniente 100, Del Valle Sector Fatima, 64000 Monterrey, Nuevo Leon, Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Irlandes de Monterrey", "Eje Metropolitano 11, Zona San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico",
        "Av. Batallon de San Patricio, Zona San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Mano Amiga La Cima", "Aluminio 633-634, San Pedro 400, 66210 San Pedro Garza Garcia, N.L., Mexico",
        "Tungsteno 630, San Pedro 400, 66210 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Mater", "Unnamed Road, Carrizalejo, 66266 San Pedro Garza Garcia, N.L., Mexico",
        "Eje Metropolitano 9, Zona Santa Barbara, San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto San Roberto", "Av Lampazos 101-113, Zona San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico",
        "Av Lampazos 216-210, Zona San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Instituto Welfare", "Av. Ignacio Morones Prieto, Zona Los Callejones, 66230 San Pedro Garza Garcia, N.L., Mexico",
        "Av. Ignacio Morones Prieto, Zona Los Callejones, 66230 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Liceo Anglo Frances de Monterrey", "Rio de la Plata 195-125, Del Valle, 66220 San Pedro Garza Garcia, N.L., Mexico",
        "Rio de la Plata 100-103, Del Valle, 66220 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Liceo de Monterrey - Campus Valle Oriente", "Jose Maria Escriva, Zona Loma Larga Oriente, San Pedro Garza Garcia, N.L., Mexico",
        "Jose Maria Escriva, Zona Loma Larga Oriente, San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Necali Centro Educativo", "Av Alfonso Reyes, Zona San Agustin Campestre, San Pedro Garza Garcia, N.L., Mexico",
        "Av Alfonso Reyes 801-717, Zona San Agustin Campestre, San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Pan American School", "EDIFICIO LOSOLES PB14, Av Lazaro Cardenas 2400, Zona Loma Larga Oriente, 66267 San Pedro Garza Garcia, N.L., Mexico",
        "Unnamed Road, Zona Loma Larga Oriente, San Pedro Garza Garcia, Nuevo Leon, Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Preparatoria UDEM", "Av. Jose Calderon A., Nuevo Leon, Mexico",
        "Unnamed Road, Nuevo Leon, Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Preparatoria Anahuac - Irlandes", "Eje Metropolitano 11, Zona San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico",
        "Av. Batallon de San Patricio, Zona San Agustin, 66278 San Pedro Garza Garcia, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("American School Foundation of Monterrey", "Francisco Villa, Cordillera, Santa Catarina, N.L., Mexico",
        "Francisco Villa 104, Cordillera, Santa Catarina, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("Preparatoria Tec - Campus Santa Catarina", "Eje Metropolitano 20, San Isidro, Santa Catarina, N.L., Mexico",
        "Eje Metropolitano 20 294, San Isidro, 66180 Santa Catarina, N.L., Mexico")''')

conn.commit()

# Create the "traffic" table.

cursor.execute('''CREATE TABLE traffic
        (traffic_id integer PRIMARY KEY, route_name text, date_time text, distance integer,
        duration_traffic integer, velocity integer, avg_delay integer,
        FOREIGN KEY (route_name) REFERENCES routes (route_name)) ''')

conn.close()