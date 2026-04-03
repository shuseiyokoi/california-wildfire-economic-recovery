# Climate and Mobility Shock Detection for Economic Activity Forecasting
_This project explores whether mobility, weather, and related external signals can detect early economic disruptions before official indicators are released. It also examines how quickly regional and urban economic systems recover after extreme events such as wildfires and severe weather._

# Research questions

## 1. Early disruption detection
Can we detect early economic disruptions using mobility, weather, and energy-related signals?

Do extreme weather deviations combined with mobility contraction predict short-term regional economic slowdown before official indicators?

## 2. Extreme event impact detection
Can we quantify how fast urban and regional systems recover after extreme events such as wildfires, storms, and other disasters?

# Data sources

## 1. CAL FIRE Wildfire Incident Data
Used to identify wildfire events and affected counties in California.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| CAL FIRE incidents | incident name, county, incident date, acres burned, location | Identify wildfire shocks and affected regions |

Source: CAL FIRE Incidents  
https://www.fire.ca.gov/incidents

## 2. BLS Quarterly Census of Employment and Wages (QCEW)
Used to measure county-level labor market conditions.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| BLS QCEW | employment, wages, county, industry, quarter | Measure local labor market changes after shocks |

Source: BLS QCEW Downloadable Data Files  
https://www.bls.gov/cew/downloadable-data-files.htm

## 3. NOAA Storm Events Database
Used to capture extreme weather events beyond wildfire incidents.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| NOAA Storm Events Database | storm type, event date, location, damage indicators | Identify weather-related shocks and compare recovery patterns |

Source: NOAA Storm Events Database  
https://www.ncei.noaa.gov/stormevents/ftp.jsp

## 4. ERA5 Reanalysis
Used to measure weather deviations and environmental conditions.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| ERA5 Reanalysis | temperature, precipitation, wind, other atmospheric variables | Build weather anomaly features and extreme event indicators |

Sources:  
https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5  
https://www.ecmwf.int/en/forecasts/datasets

## 5. Google Community Mobility Reports
Used as a mobility-based proxy for economic disruption.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| Google Community Mobility Reports | mobility changes by region and category | Detect contraction in movement and activity patterns |

Source: Google Community Mobility Reports  
https://www.google.com/covid19/mobility/

<!-- Data availability appears limited to around 2020 -->
<!-- Confirm final usable coverage before analysis -->

## 6. Opportunity Insights Economic Tracker
Used as a high-frequency economic activity source.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| Opportunity Insights Economic Tracker | economic activity indicators, consumer and regional metrics | Track short-term economic disruptions and recovery |

Source: Opportunity Insights Economic Tracker  
https://economictracker.org/

<!-- Coverage may be limited and should be verified -->
<!-- Consider alternative metrics if data is not recent enough -->

## 7. Bureau of Economic Analysis (BEA)
Used to measure county-level economic output.

| Data source | Variables / coverage | Purpose |
|-------------|----------------------|---------|
| BEA GDP by county, CAGDP2 | GDP by county, GDP by industry, annual output | Measure broader regional economic performance |

Source: Bureau of Economic Analysis  
<!-- add exact BEA API or table link if you use one -->

### Notes on BEA data
- Table: **Gross Domestic Product by County**
- Dataset: **CAGDP2 GDP by industry in current dollars**
- Geography: **State / County**
- Data range noted: **2001 to 2024**
- Units may include:
  - Level (thousands of current dollars)
  - Percent change from preceding period
  - Compound annual growth rate between any two periods
  - Index based on earliest selected year

# Results
<!-- Results not available yet -->
_Results are not available yet. This section will summarize whether weather anomalies, mobility contraction, and extreme event exposure can help detect short-term economic slowdown and recovery before official indicators are released._

# Installation
- Install required Python packages from `requirements.txt` if provided.
- Add API keys to `.env` only if any API-based data access is used.
- No required API key information is currently provided.

<!-- Remove packages not used in the final version -->
Suggested packages:
- `pandas`
- `numpy`
- `requests`
- 

# Running analysis

From `src/` directory run:

`python main.py`

Results will appear in `results/` folder.  
All obtained data will be stored in `data/`.

<!-- Update this if the real entry point is different -->
<!-- If notebooks are used for the main workflow, document that here -->

# Relevant papers
Eckert, Florian, et al.. “Tracking Economic Activity With Alternative High-Frequency Data.” Journal of Applied Econometrics, vol. 40, no. 3, 2025, pp. 270-90. [https://www.research-collection.ethz.ch/server/api/core/bitstreams/88127dde-7a15-4726-b5ec-69427e390125/content](https://www.research-collection.ethz.ch/server/api/core/bitstreams/88127dde-7a15-4726-b5ec-69427e390125/content).
Kim, E., & Kwon, Y. J.. “Analyzing indirect economic impacts of wildfire damages on regional economies.” Risk Analysis, vol. 43, no. 12, 2023, pp. 2631–43. [https://doi.org/10.1111/risa.14106]([url](https://doi.org/10.1111/risa.14106)). 
Zhiyun Li, William Yu. “Economic Impact of the Los Angeles Wildfires.” UCLA Anderson School of Management, https://www.anderson.ucla.edu/about/centers/ucla-anderson-forecast/economic-impact-los-angeles-wildfires.
