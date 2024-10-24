# WM-Gym-Performance

<div align="center">
  <img src="https://github.com/user-attachments/assets/6611517a-21a9-431a-86f8-e0fda7cc28fa" alt="Screenshot 2024-10-24 130000" width="500"/>
  <br></br>
</div>

Extraction and Visualization of William and Mary's D1 Men's Gymnastics team's scores from 2020 to 2024 of both team and individual scale.

## Technology
- Excel
- Python
  - pandas
- R/Rmarkdown
  - Tidyverse, ggplot
- PostegeSQL
- Tableau
- Streamlit

## Workflow

### Data Extraction/Collection

The only available data I could find was in the form of pdfs for each season on William and Mary's official website. 

- I first converted the the pdf data to xlsx with a simple google converting.
- Reformatted the converted data within Excel to eliminate inconsistencies and maintain uniform formatting.
- Exported from Excel to Python notebook for further preperation.

### Data Cleaning

- Used Python to remove unneccessary data, duplicates, and missing data.
- Convert string dates into datetime objects.
- Prepared data for entry into SQL database.

### Database construction

- Created and connected to PostgreSQL with Python
- Used SQL to design and enter data in tables

### Data Exploration

- Used R to connect to SQL database and group data for visualization. Also played around with time series; however, irregularly spaced time series present problems with accuracy.
- Used Tableau to explore data holistically (combined to represent team performance.

### Visualization

- Used R loop to generate individual pdf files for each athletes performance over every season they participated in.
  - scatter and line plots, created with ggplot, are used to visualize performance
- Visualized team performance over 4 seasons dynamically with Tableau
  - Published Tableau dashboard with streamlit.
