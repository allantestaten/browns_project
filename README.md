# Predicting Outcome of Browns Football Game
 
# Project Description
This project is focused on analyzing the team statistics of the Cleveland Browns football team to determine the drivers that determine the outcome of the game. 
 
# Project Goal
* Identify drivers that have a significant relationship to the outcome of the game.  
* Develop and use machine learning model to accurately predict outcome of the game. 
* Deliver a report of the project in a final notebook.
* Deliver a report that explains what steps were taken and why they were taken.

# Executive Summary 
* In this dataset Browns lose more games than they win
* 4 Models were created, Best model performs 42% better than the baseline model 
* drivers of target variable : two hundred yards gained, under 300 total yards allowed and less than two turnovers 
* The browns should game plan to rush for more than 200 yards per game, allow less than 300 total yards on defense and turn the ball over less than two times each game 

# Initial Thoughts
The browns rushing yards, turnovers and amount of yard given up by the defense per game would contribute to the outcome of the game. 

# The Plan
* Data Acquisition
    * This data was acquired on Dec 21 from https://www.pro-football-reference.com/teams/cle/2022.htm
    * Download the Schedule & Game Results for the 2019, 2020, 2021 and 2022 season 
    * Combine the data of the seasons downloaded into one document to read into jupyter notebook

 
* Prepare data
   * Deleted top row of excel sheet 
   * Dropped columns 
        * Week
        * Day
        * Date
        * Unnamed: 3  
        * Unnamed: 4
        * OT 
        * Rec
    * Remove the bye weeks from each season 
    * Remove the last three columns of the excel sheet
    * Renamed columns to more readable names 
    * Performed get dummies on region, retailer, product and sales method columns 
    * Replaced spaces with underscores and made all words lower case
    * Convert all numerical columns to integer data types 

 
* Explore data in search of drivers of game result
   * Answer the following initial questions
       * What is the mode of the result?
       * Have the Browns won more games at home or away? 
       * Is there a significant difference in the mean of rush yards in games resulting in wins compared to all games?
       * Is there a significant difference in the mean of turnovers in games resulting in wins compared to all games?
       * Is there a significant difference in the mean between rushing for more than 200 yards in games resulting in wins compared to all games?
       * Is there a significant difference in the mean of games where total yards allowed is less than 300 yards compared to all games?
       * Is there a significant difference in the mean of games where turnovers are less than 2 compared to all games? 

      
* Develop a Model to predict an accurate value of the operating margin
   * Use drivers supported by statistical test results to build predictive models
   * Evaluate all models on train 
   * Evaluate top models on validate data 
   * Select the best model based on best accuracy with awareness of over fitting
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Result| outcome of the game: W (win) or L(loss)|
|Location| Where is the game played: home (at brown's stadium) or away(not brown's staidum)|
|Two Hundred Yards Gained| Number of Yards Rushed For: 1 (Browns rushed for more than 200 yards in a win), 0 (Browns did not rush for more than 200 yards in a win) |
|Under 300 Total Yards Allowed| Browns Defense allowed less than 300 total yards: 1 (Browns defense gave up less than 300 Total Yards Allowed), 0 (Browns did not rush for more than 200 yards in a win)|
|Less than Two Turnovers| Number of Games with Less than Two Turnovers: 1 (Browns had less than two turnovers in a game Won),  (Browns did not have less than two turnovers in a game Won)|

# Steps to Reproduce
1) Clone this repo
2) Acquire the data from https://www.pro-football-reference.com/teams/cle/2022.htm
3) Create one consolidated excel document of data
4) Delete top row of excel sheet
5) Remove the last three columns of the excel sheet
6) Run notebook


# Takeaways and Conclusions
- Operating margin has a relationship with region,retailer,sale method and product 
- Women's apparel and men's street footwear appear to have the highest profit margins
- Online Sales appears to have the highest operating margin 
- The retailer with the highest operating margin is sports direct
- Walmart appears to be underperforming relative to its peers
- South region has the highest operating margin 
- Operating Margin has few outliers considering the difference median and mean are approximately 1% 

# Recommendations
* Provide Walmart less inventory and shift inventory to better performing retailer
* The sales department reach out to the retailer sports direct to find out if they are opening more locations

# Next Steps
* Research if data supports decreasing the number of stores in certain cities or states based on how much of their operating margin comes from online sales  