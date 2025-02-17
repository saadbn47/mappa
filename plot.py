import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

from flask import Flask, request, render_template, jsonify
app = Flask(__name__,
    template_folder='templates',
    static_folder='static'
)


# Load GeoJSON data
def load_geojson_data(file_path='static/bordeaux_data.geojson'):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Convert GeoJSON to DataFrame
def geojson_to_df(geojson_data):
    rows = []
    for feature in geojson_data['features']:
        properties = feature['properties']
        properties['Longitude'] = feature['geometry']['coordinates'][0]
        properties['Latitude'] = feature['geometry']['coordinates'][1]
        rows.append(properties)
    return pd.DataFrame(rows)

# Create boxplot for specific IRIS code
def create_iris_boxplot(df, iris_code):
    # Filter data for the specified IRIS code
    df_iris = df[df['code_iris'] == iris_code]
    
    if df_iris.empty:
        print(f"No data found for IRIS code: {iris_code}")
        return None
    
    # Create the boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='code_iris', y='valeur_fonciere/m²', data=df_iris)
    plt.title(f'Distribution des valeurs foncières - Code IRIS: {iris_code}')
    plt.xlabel('Code IRIS')
    plt.ylabel('Valeur Foncière par m²')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('static/boxplots.png')
    plt.close()
    
    return True

# Add these routes after your existing functions
@app.route('/')
def index():
    return render_template('site.html')

@app.route('/generate_boxplot', methods=['POST'])
def generate_boxplot():
    try:
        iris_code = request.form.get('iris_code')
        if not iris_code:
            return jsonify({'success': False, 'error': 'No IRIS code provided'})
        
        # Load data
        geojson_data = load_geojson_data()
        df = geojson_to_df(geojson_data)
        
        # Generate boxplot
        result = create_iris_boxplot(df, iris_code)
        return jsonify({'success': result is not None})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)