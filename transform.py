import csv
import json

# Chemin vers le fichier CSV
csv_file_path = 'df_bdx_pred.csv'

# Chemin vers le fichier GeoJSON de sortie
geojson_file_path = 'bordeaux_data.geojson'

# Lire les données du CSV
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    features = []
    for row in reader:
        # Créer une feature GeoJSON pour chaque ligne du CSV
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(row["Longitude"]), float(row["Latitude"])]
            },
            "properties": {
                "Date mutation": row["Date mutation"],
                "No voie": row["No voie"],
                "Valeur fonciere": row["Valeur fonciere"],
                "Type local": row["Type local"],
                "Surface reelle bati": row["Surface reelle bati"],
                "Nombre pieces principales": row["Nombre pieces principales"],
                "Adresse complète": row["Adresse complète"],
                "valeur_fonciere/m²": row["valeur_fonciere/m²"],
                "code_iris": row["code_iris"],
                "nom_iris": row["nom_iris"],
                "Year": row["Year"],
                "Quarter": row["Quarter"],
                "nb_arret_bus": row["nb_arret_bus"],
                "nb_arret_tram": row["nb_arret_tram"],
                "nb_ecoles_elementaire": row["nb_ecoles_elementaire"],
                "nb_ecoles_maternelle": row["nb_ecoles_maternelle"],
                "nb_ecoles_maternelle,elementaire": row["nb_ecoles_maternelle,elementaire"],
                "code_iris_freq": row["code_iris_freq"],
                "code_iris_encoded": row["code_iris_encoded"],
                "nb_autoroute": row["nb_autoroute"],
                "nb_chemin rural": row["nb_chemin rural"],
                "nb_route départementale": row["nb_route départementale"],
                "nb_route nationale": row["nb_route nationale"],
                "nb_voie métropolitaine": row["nb_voie métropolitaine"],
                "nb_voie privée": row["nb_voie privée"],
                "ABCDE": row["ABCDE"],
                "C21_F15P_CS3": row["C21_F15P_CS3"],
                "P21_POP0305": row["P21_POP0305"],
                "C21_POP15P_CS3": row["C21_POP15P_CS3"],
                "P21_POP0610": row["P21_POP0610"],
                "C21_H15P_CS6": row["C21_H15P_CS6"],
                "P21_POP5564": row["P21_POP5564"],
                "C21_H15P_CS7": row["C21_H15P_CS7"],
                "P21_H4559": row["P21_H4559"],
                "C21_H15P_CS3": row["C21_H15P_CS3"],
                "C21_F15P_CS5": row["C21_F15P_CS5"],
                "y_pred": row["y_pred"]
            }
        }
        features.append(feature)

# Créer l'objet GeoJSON
geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Écrire les données GeoJSON dans le fichier de sortie
with open(geojson_file_path, 'w', encoding='utf-8') as geojsonfile:
    json.dump(geojson, geojsonfile, ensure_ascii=False, indent=4)

print(f"Les données ont été converties en GeoJSON et enregistrées dans {geojson_file_path}")