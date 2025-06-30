# python-dev-intern-task-5-data-analysis-on-csv-files
Python Developer Internship Task 5 (Data Analysis on CSV files)

## CSV File ##
Get sample CSV file from https://github.com/datablist/sample-csv-files?tab=readme-ov-file
or 
https://excelbianalytics.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/

1. Install Pandas
>>> pip install pandas
2. Code and run python main.py

Jupyter notebook − A web based interface to programming environments of Python
Jupyter Notebook is a free, open-source web app that lets you create and share documents with live code and visualizations. It is commonly used for tasks like cleaning and transforming data, doing statistical analysis, creating visualizations and machine learning.

Matplotlib is a popular Python library for creating 2D plots. 

>>> pip install matplotlib

Importing matplotlib in Jupyter Notebook is easy; you can use this command to do that:

>>> python matplot.py

opens a new Figure window.

## Now Task ##
1. File created - data_analyzer.py
2. Our CSV sales file info
 - Columns - Region, Country, Item Type, Sales Channel, Order Priority, Order Date, Order ID, Ship Date, Unit Sold, Unit Price, Unit Cost, Total Revenue, Total Cost, Total Profit
3. Read CSV
4. Group by - Region
5. Find Sum - Total Revenue
6. Plot it
7. Run >>> python data_analyzer.py

## To deliver a Matplotlib visualization within a Jupyter Notebook ##

To create a Jupyter Notebook that reads data from a CSV file and visualizes it using Matplotlib, follow these steps:
1. Launch Jupyter Notebook: >>> jupyter notebook
[I 2025-06-30 17:23:47.964 ServerApp] Jupyter Server 2.16.0 is running at:
[I 2025-06-30 17:23:47.964 ServerApp] http://localhost:8889/tree?token=a6fd49fd9b0b9b3356ab2a4bd84d33194d543c601891cb3f
[I 2025-06-30 17:23:47.964 ServerApp]     http://127.0.0.1:8889/tree?token=a6fd49fd9b0b9b3356ab2a4bd84d33194d543c601891cb3f
[I 2025-06-30 17:23:47.965 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
This will open a new tab in your web browser with the Jupyter Notebook interface. All the files and folders are listed.
2. Click New->Select Python 3 to create a new Notebook
3. CSV file is in same directory
4. In first cell
write
  import pandas as pd
  import matplotlib.pyplot as plt
5. Next Cell
  df = pd.read_csv("100 Sales Records.csv")
6. Next cell -- add remining code.
7. Run each cell and got the graph.
8. Save your Jupyter Notebook by clicking "File" -> "Save and Checkpoint" as sales_data_analyzer.ipynb file.
http://localhost:8889/notebooks/sales_data_analyzer.ipynb
This process enables the creation of interactive documents containing live code, visualizations, and explanatory text, making them ideal for data exploration, analysis, and sharing.

## Deliverables: ##
1. sales_data_analyzer.ipynb
2. Share as HTML
>>> jupyter nbconvert sales_data_analyzer.ipynb --to html
File --> sales_data_analyzer.html


## Sharing as PDF ##
  - Download and Install Pandoc
  - https://github.com/jgm/pandoc/releases/tag/3.3 MSI file
  - restart CMD
  - pandoc --version
  - Download and install MiKTeX https://miktex.org/download
  - jupyter nbconvert sales_data_analyzer.ipynb --to latex
  - Restart CMD
  - pdflatex sales_data_analyzer.tex ()
  - Not working