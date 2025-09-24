# [Web App](https://guinea-pig-portfolio.onrender.com/)
---
Welcome to the code for my portfolio simulator web app called Guinea Pig Portfolio

This repository is aligned with Django's framework. 

The Index data folds holds files resposible for importing data from https://site.financialmodelingprep.com/ and the associated API. The create data and insert data scripts lean on the PostgreSQL instance connected to Django and fill out the respective tables with data for use in the modelling or portfolios later on.

The guinea_pig directory handles the base of the site and houses django settings. The user app/directory handles users and logging in. The portfolio tester directory/app models portfolios and stores/reads previously submitted portfolios.

To clone this repository and run the code, you will need to obtain an API key from Financial Modeling Prep and set up a SQL (PostgreSQL external, SQLite locally, etc.) to house data and set up Django's back end.


