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


## 3. Bureau of Economic Analysis (BEA)
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
