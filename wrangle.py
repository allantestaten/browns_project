import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as plt 
from sklearn.model_selection import train_test_split
from scipy import stats



#------------------GET DATA-------------------------------
def acquire_prep_data():
    '''this function will retrieve the data and clean it'''
    #get a data 
    df = pd.read_excel('consolidated record.xls')
    # dropping columns 
    df = df.drop(columns= ['Week','Day','Date','Unnamed: 3','Unnamed: 4','OT','Rec'])
    # replace spaces with underscore and make words lowercase 
    df.columns = [column.replace(' ','_').lower() for column in df]
    # renaming column names to more readable format
    df = df.rename(columns = {'unnamed:_5':'result', 'opp':'opponent',
                              'opp.1':'points_allowed', 
                              'tm':'points_scored',
                              '1std_o':'first_downs_gained', 'totyd_o_':'total_yards_gained',
                              'passy_o_':'pass_yards_gained',
                              'rushy_o_':'rush_yards_gained','to_o_':'turnovers','1std_d_':'first_downs_allowed',
                              'totyd_d_':'total_yards_allowed',
                              'passy_d_':'pass_yards_allowed','rushy_d_':'rush_yards_allowed',
                              'to_d_':'turnovers_forced',})
    # fill all nans with zero value 
    df = df.fillna(0)
    # replace zeros in location with word home and replace @ symbol with away 
    df['location'] = df['location'].replace([0, '@'], ['home', 'away',])
    # Converting data types to integers 
    df.astype({'turnovers':'int64','turnovers_forced':'int64'}).dtypes

    return df



def split_data(df):
    '''this function splits the data into train validate and test datasets'''
    # splitting data into test and validate samples 
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.result)
    # splitting data into train and validate samples 
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.result)

    return train, validate, test
#------------------Visualizations-------------------------------

def countplot(data,x,hue):
    '''this function creates a countplot'''
    sns.countplot(data=data, x=x, hue=hue).set(title='Result by Location')

def histogram_rush_wins(train):
    '''visualization for games won and rushing yards'''
    # rush yards in games won 
    rush_sample_won = train[train.result == "W"].rush_yards_gained
    #histogram of rush yards in games won 
    rush_sample_won.plot(kind='hist', title='Rush Yards in Games Won')

def histogram_rush_loss(train):
    '''visualization for games lost and rushing yards'''
    # rush yards in games lost 
    rush_sample_loss = train[train.result == "L"].rush_yards_gained
    #histogram of rush yards in games lost 
    rush_sample_loss.plot(kind='hist', title='Rush Yards in Games lost')

def histogram_forced_turnovers_wins(train):
    '''visualization for games won and forced turnovers'''
    # forced turnoveres in games won 
    turnovers_forced_win = train[train.result == "W"].turnovers_forced
    #histogram of rush yards in games won 
    turnovers_forced_win.plot(kind='hist', title='Turnovers Forced in Games Won')

def histogram_forced_turnovers_loss(train):
    '''visualization for games lost and forced turnovers'''
    # forced turnovers in games lost 
    turnovers_forced_loss = train[train.result == "L"].turnovers_forced
    #histogram of rush yards in games lost 
    turnovers_forced_loss.plot(kind='hist', title='Turnovers Forced in Games lost')

def histogram_total_yards_allowed_wins(train):
    '''visualization for games won and total yards allowed'''
    # total yards allowed in games won 
    total_yards_allowed_win = train[train.result == "W"].total_yards_allowed
    #histogram of rush yards in games won 
    total_yards_allowed_win.plot(kind='hist', title='Total Yards Allowed in Games Won')

def histogram_total_yards_allowed_loss(train):
    '''visualization for games lost and total yards allowed'''
    # total yards allowed in games lost 
    total_yards_allowed_loss = train[train.result == "L"].total_yards_allowed
    #histogram of rush yards in games lost 
    total_yards_allowed_loss.plot(kind='hist', title='Total Yards Allowed in Games lost')
#------------------Statistical tests-------------------------------

def chi_square(df,column_a,column_b):
    '''this function will chi square test results '''
    # cross tab created in preparation to run chi^2 test
    observed = pd.crosstab(df[column_a], df[column_b])
    #code to generate results of chi^2 test 
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p}')

def ttest_ind_rushing(train):
    '''statistical test and results'''
    # creating variable to represent rushing yards in games lost
    rush_sample_loss = train[train.result == "L"].rush_yards_gained
    # creating variable to represent rushing yards in games won
    rush_sample_won = train[train.result == "W"].rush_yards_gained
    # stats test 
    t, p = stats.ttest_ind(rush_sample_loss, rush_sample_won,equal_var=False)
    print(f't = {t:.4f}')
    print(f'p/2     = {p/2}')

def ttest_ind_forced_turnovers(train):
    '''statistical test and results'''
    # creating variable to represent forced turnovers in games lost
    forced_turnovers_loss_sample = train[train.result == "L"].turnovers_forced
    # creating variable to represent forced turnovers in games won
    forced_turnovers_won_sample = train[train.result == "W"].turnovers_forced
    # stats test 
    t, p = stats.ttest_ind(forced_turnovers_loss_sample, forced_turnovers_won_sample,equal_var=False)
    print(f't = {t:.4f}')
    print(f'p/2     = {p/2}')

def ttest_ind_forced_turnovers(train):
    '''statistical test and results'''
    # creating variable to represent forced turnovers in games lost
    forced_turnovers_loss_sample = train[train.result == "L"].turnovers_forced
    # creating variable to represent forced turnovers in games won
    forced_turnovers_won_sample = train[train.result == "W"].turnovers_forced
    # stats test 
    t, p = stats.ttest_ind(forced_turnovers_loss_sample, forced_turnovers_won_sample,equal_var=False)
    print(f't = {t:.4f}')
    print(f'p/2     = {p/2}')

def ttest_ind_total_yards_allowed(train):
    '''statistical test and results'''
    # creating variable to represent forced turnovers in games lost
    total_yards_allowed_loss_sample = train[train.result == "L"].total_yards_allowed    # creating variable to represent forced turnovers in games won
    total_yards_allowed_won_sample = train[train.result == "W"].total_yards_allowed    # stats test 
    t, p = stats.ttest_ind(total_yards_allowed_won_sample, total_yards_allowed_loss_sample,equal_var=False)
    print(f't = {t:.4f}')
    print(f'p/2     = {p/2}')


