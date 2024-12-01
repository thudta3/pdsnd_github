import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
"""function to get user input for city (chicago, new york city, washington)"""
def get_city():
    city_list = ["chicago", "new york", "washington"]
    city = input('Would you like to see data for Chicago, New York or Washington?\n ').lower()
    while city not in city_list:
        print('Invalid input. Please input from Chicago, New York or Washington')
        city = input('Would you like to see data for Chicago, New York or Washington?\n ').lower()
    return city

"""function to get user time from both, month, day, none"""
def get_time():
    time = ['both', 'month', 'day', 'none']
    user_time = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n ')
    while user_time not in time:
        print('Invalid input. Please input from month, day, both or none')
        user_time = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n ')
    return user_time
            
"""function to get user input for month (all, january, february, ... , june)"""
def get_month():
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Which month? Please type your response by "all", "january", "february", "march", "april", "may", "june".\n ')
    while month not in months:
        print('Invalid input. Please input again')
        month = input('Which month? Please type your response by "all", "january", "february", "march", "april", "may", "june".\n ')
    return month  
        
"""function to get user input for day of week (all, monday, tuesday, ... sunday) """
def get_day():
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Which day? Please type your response by "all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday".\n ')
    while day not in days:
        print('Invalid input. Please input again')
        day = input('Which day? Please type your response by "all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday".\n ')
    return day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month']==month.title()]
    if day != 'all':
        df = df[df['day']==day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular hour:', popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination_station = df['Start Station'].mode()[0] + ' to ' + df['End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip:', common_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ('The total travel time is: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print ('The mean travel time is: ',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('What is the breakdown of User Type?')
    print(user_type)

    # TO DO: Display counts of gender
    if ('Gender' not in df):
        print('Sorry! No gender data to share')
    else:
        user_gender = df['Gender'].value_counts()
        print('What is the breakdown of gender?')
        print(user_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('Sorry! No Birth Year data to share')
    else:
        user_birth_year_min = df['Birth Year'].min()
        user_birth_year_max = df['Birth Year'].max()
        user_birth_year_common = df['Birth Year'].mode()[0]
        print('What is the oldest, youngest, and most popular year of birth?')
        print('The oldest Birth Year:', user_birth_year_min)
        print('The youngest Birth Year:', user_birth_year_max)
        print('The most popular year of birth:', user_birth_year_common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    while start_data < df_length:
        raw_data = input("\nWant to see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':
            print("\nDisplaying only 5 rows of data.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break
            
def main():
    while True:
        print('Hello! Let\'s explore some US bikeshare data!')
        
        """Get user input for city"""
        city = get_city()

        """Get user input for time filter (month, day, both, or none)"""
        time = get_time()

        """Initialize month and day as None"""
        month = None
        day = None

        """Get additional input based on time filter"""
        if time == 'both':
            month = get_month()
            day = get_day()
        elif time == 'month':
            month = get_month()
        elif time== 'day':
            day = get_day()
      
        """Load the data"""
        df = load_data(city, month, day)
        
        """Display statistic result"""
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
