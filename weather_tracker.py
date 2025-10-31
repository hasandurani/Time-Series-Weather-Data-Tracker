import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

def fetch_weather_data(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Data has been successfully retrieved from the API.")
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not retrieve data from the API - {e}")
        return None

def process_and_visualize_data(weather_data):
    if not weather_data:
        print("Weather data is not available for visualization.")
        return

    hourly_data = weather_data['hourly']
    df = pd.DataFrame(hourly_data)
    
    df['time'] = pd.to_datetime(df['time'])
    
    print("\nWeather Data Summary:")
    print(df.head())

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    ax1.plot(df['time'], df['temperature_2m'], label='Temperature (°C)', color='red')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_title('Analysis of Temperature and Humidity Over Time')
    ax1.legend()
    ax1.grid(True)
    
    ax2.plot(df['time'], df['relative_humidity_2m'], label='Humidity (%)', color='blue')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Relative Humidity (%)')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    
    plt.savefig('weather_data_visualization.png')
    print("\nVisualization has been saved as 'weather_data_visualization.png'.")
    
    plt.show()

if __name__ == "__main__":
    # Enter the Latitude and Longitude for your city here
    # Example for Karachi: Latitude: 24.8607, Longitude: 67.0011
    city_latitude = 24.8607
    city_longitude = 67.0011
    
    data = fetch_weather_data(city_latitude, city_longitude)
    
    process_and_visualize_data(data)
