IOT Project to take data from sensors and store it
Techstack - Django, DRF, Docker

#How to run
1. git clone <repo>
2. cd <repo>
3. docker-compose up --build

   Now you can access Browsable APIs from browser and also from postman
   
1. localhost:8000/api/sensor - CRUD operations for sensor
2. localhost:8000/api/sensor-data - CRUD operations for sensor-data
3. localhost:8000/api/token - Get access token for provided user credentials ( valid for 24 hours)
4. localhost:8000/api/token/refresh - Get new access token with refresh token after expiration
