import requests
import pandas as pd
import json
import prettytable

class get_major_indicators():
    
    def __init__(self, series_id):
        
        # inputs
        self.series_id = series_id
        
        # outputs
        self.fetch_data = self.fetch_data()
        self.gdp = self.get_gdp()
        self.real_gdp = self.get_real_gdp()
        self.gdp_pct_change = self.get_gdp_pct_change()
        
        def fetch_data(self):
            
            series_id = self.series_id
            
            """Fetch observations for a FRED series and save to a DataFrame."""
            url = f"https://api.stlouisfed.org/fred/series/observations"
            
            api_key = "9648695895d3facac4fba9c7cb834427"
            
            params = {
                "series_id": series_id,
                "api_key": api_key,
                "file_type": "json"
            }
            response = requests.get(url, params=params)
            

            data = response.json()
            observations = data.get('observations', [])
            # Create DataFrame
            df = pd.DataFrame(observations)
            # Display the DataFrame
            
            return df

        

            
    