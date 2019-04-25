# NYU Taxi Prediction
It is a capstone project that requires to create custom features to understand NYC taxi trip patterns, based on the existing dataset. The dataset is from the classic NYC taxi trip dataset from Kaggle. The aim is to predict the travel time according to other features.

## Features for the prediction
1. __id__: Each driveer has a special ID
2. __pickup_datetime__: The day and the exact time the driver picks up passengers
3. __dropoff_datetime__: The day and the exact time the driver drops off passengers
4. __passenger_count__: The number of passengers on taxi
5. __trip_distance__: The total length of the journey (km)
6. __pickup_longitude/pickup_latitude__: The location (or coordinate) of the pickup position
7. __dropoff_longitude/dropoff_latitude__: The location (or coordinate) of the dropoff position
8. __payment_type__: 1 - Credit card; 2 - Cash; 3 - No payment; 4 - Dispute
9. __trip_duration__: The duration of the trip in minutes
10. __pickup_neighbourhood/dropoff_neighbourhood__: Pickup/Dropoff area that is named in area code

## EDA
1. Histgram: It is used to gain an insight of the target column

![alt text](https://github.com/KaitaiD/Capstone-Project-1/blob/master/1.JPG)

2. lmplot: It is used to see the linear inter-relationship between the features and target

![alt text](https://github.com/KaitaiD/Capstone-Project-1/blob/master/2.JPG)

3. pairplot: It is for the inner patterns between the pickup/dropoff location, trip duration and payment

![alt text](https://github.com/KaitaiD/Capstone-Project-1/blob/master/3.JPG)

## Prediction
A number of feature engineering is done to obtain the best prediction result. For example, pickup and dropoff time is expanded in the code to check if it is in the weekend.
