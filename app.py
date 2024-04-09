import streamlit as st
import pickle
import pandas as pd
import numpy as np
# import xgboost
# from xgboost import XGBRegressor

pipe = pickle.load(open('pipe.pkl','rb'))


teams = ['Australia', 'Sri Lanka', 'India', 'England', 'Pakistan',
       'South Africa', 'New Zealand', 'West Indies', 'Bangladesh', 'Zimbabwe',
       'Afghanistan', 'Ireland']

cities = ['Belfast', 'Mirpur', 'Cape Town', 'Johannesburg', 'Sharjah',
       'Abu Dhabi', 'Kolkata', 'Bulawayo', 'St Lucia', 'Cardiff',
       'Chandigarh', 'Centurion', 'Melbourne', 'Chattogram', 'Fatullah',
       'Trinidad', 'Nottingham', 'Sydney', 'Christchurch', 'Barbados',
       'Chittagong', 'Leeds', 'Cuttack', 'Grenada', 'Durban', 'Guyana',
       'St Kitts', 'Southampton', 'Brisbane', 'Colombo', 'Perth',
       'Pallekele', 'Rawalpindi', 'Dublin', 'Taunton', 'Antigua',
       'Harare', 'Hamilton', 'Manchester', 'Indore', 'Pune', 'Dehra Dun',
       'Adelaide', 'Bristol', 'Mumbai', 'Birmingham', 'London',
       'Wellington', 'Mount Maunganui', 'Faisalabad', 'Queenstown',
       'Kochi', 'Port Elizabeth', 'Lucknow', 'Auckland', 'Bloemfontein',
       'Visakhapatnam', 'Delhi', 'Vadodara', 'Dubai', 'Edinburgh',
       'Rajkot', 'Dunedin', 'Lahore', 'Ahmedabad', 'Hobart', 'Ranchi',
       'Hyderabad', 'Kimberley', 'Hambantota', 'Dhaka', 'Karachi',
       'Jamaica', 'Guwahati', 'Rangiri', 'Potchefstroom', 'Multan',
       'Bridgetown', 'Kanpur', 'St Vincent', 'Darwin', 'Napier', 'Bogra',
       'Deventer', 'Sylhet', 'Jaipur', 'Margao', 'Kuala Lumpur',
       'Gwalior', 'Whangarei', 'Chester-le-Street', 'Nagpur',
       'East London', 'Nelson', 'Canberra', 'Dominica', 'Chennai',
       'Benoni', 'Bengaluru', 'Paarl', 'Greater Noida', 'Bangalore',
       "St George's"]

st.title("Cricket score prediction")

col1,col2 = st.columns(2)

with col1:
    battingTeam = st.selectbox("Select Batting Team",sorted(teams))
with col2:
    bowlingTeam = st.selectbox("Select Bowling Team",sorted(teams))

city = st.selectbox("Select The city",sorted(cities))



col3,col4,col5 = st.columns(3)


with col3:
    currentScore = int(st.number_input("Current Score"))
with col4:
    overs = int(st.number_input("Overs Done"))
with col5:
    wickets = int(st.number_input("Wickets out"))

lastFive = st.number_input("Enter the Last Five Over Score")



if(st.button("Predict Score")):
    ballsLeft = 300-overs*6
    wicketsLeft = 10-wickets
    crr = currentScore/overs
    inputDf = pd.DataFrame(
     {'batting_team': [battingTeam], 'bowling_team': [bowlingTeam],'city':city, 'current_score': [currentScore],'balls_remaining': [ballsLeft], 'wickets_left': [wicketsLeft], 'crr': [crr], 'last_five': [lastFive]})
    
    result = pipe.predict(inputDf)
    # print(result[0])
    st.header("Predicted Score -> "+str(int(result[0])))
    


# batting_team     426881 non-null  object 
#  1   bowling_team     426881 non-null  object 
#  2   city             426881 non-null  object 
#  3   current_score    426881 non-null  int64  
#  4   balls_remaining  426881 non-null  int64  
#  5   wickets_left     426881 non-null  int64  
#  6   crr              426881 non-null  float64
#  7   last_five        426881 non-null  float64
#  8   runs_x           426881 non-null  int64  