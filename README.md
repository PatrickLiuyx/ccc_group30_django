# CCC_group30_Django Backend

## Prepare ENV
Django==3.2.3, 
CouchDB==1.2,
plotly==4.14.3, 
tweepy


## Run HARVERST module to get live tweets
nohup python3  harvestest.py > python.log 2>&1 &


## Run Django Server
Python3 manage.py runserver <ip>:8000
