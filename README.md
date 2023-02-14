# Predicting Outcome of Browns Football Game
 ![](https://github.com/browns_project/browns.gif)

# Project Description
The purpose of this project is to explore the game statistics of Browns football games and come up with recommendations for the best strategy for them to win a game. I will also create a model that can accurately predict the outcome of the game. 
 
# Project Goal
* Identify drivers that have a significant relationship to the outcome of the game.  
* Develop and use machine learning model to accurately predict outcome of the game. 
* Deliver a report of the project in a final notebook.
* Deliver a report that explains what steps were taken and why they were taken.

# Executive Summary 
* Browns lose more games than they win
* Features used for model consisted of rushing yards and turnovers forced. The best model predicted the outcome of the game 4% better than the baseline
* Recommend Browns strategy to win should consist of increasing their average rushing yards on offense and average number of forced turnovers in each game on defense. 
* Next Steps consist of exploring the variables pass yards and points allowed to determine if they have a significant association with the outcome of the game

# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|result| outcome of the game: W (win) or L(loss)|
|location| home for games played at browns stadium, away for all others|
|rush_yards_gained| rushing yards achieved by browns offense |
|total_yards_allowed| total yards browns defense allowed other team's offense to achieve |
|turnovers forced| number of turnovers created by browns defense|

# Initial Thoughts
The browns rushing yards, turnovers and total yards given up by the brown's defense would contribute to the outcome of the game. 

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
       * How many games have Browns won and lost in past 3.5 sesons?
       * Is there an association between the location and result of the game?  
       * s there an association betweeen rushing yards and result of the game?
       * Is there an association betweeen turnovers forced and result of the game?
       * Is there an association betweeen total yards allowed and result of the game?

* Develop a Model to predict the outcome of a game:
   * Use drivers supported by statistical test results to build predictive models
   * Evaluate all models on train 
   * Evaluate top models on validate data 
   * Select the best model based on best accuracy with awareness of over fitting
   * Evaluate the best model on test data
 
* Draw conclusions
* Summary
    * Browns lose more games than they win 
    * Browns win more games at home then away 
    * The significant features identified during exploration were rushing yards and forced turnovers
    * The location of the game did not have an association with the result of the game 
    * The total yards allowed did not have an association with the result of the game 

* Modeling Summary
    * The features used for modeling were rushing yards gained and turnovers forced
    * The final model performed 4% better than the baseline model at predicting the result of the game
    * I would not recommend this model for production
* Recommendations
    * I would recommend the browns center their offensive strategy on rushing the ball
    * The defense should focus their strategy on playing aggressive and creating turnovers and not on how many yards they give up

* Next Steps
    * Explore if there is an association between passing yards gained and game result
    * Find out if there is a relationship between points allowed by the Browns and the outcome of the game
    * Explore more features to combine with rushing yards gained and turnovers forced to find out if that creates a better model


# Steps to Reproduce
1) Clone this repo
2) Acquire the data from https://www.pro-football-reference.com/teams/cle/2022.htm
3) Create one consolidated excel document of data
4) Delete top row of excel sheet
5) Remove the last three columns of the excel sheet
6) Run notebook


