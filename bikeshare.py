import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input ("What city are you at? Chicago, New York City or Washington?\n").lower()
        if city not in ("chicago", "new york city", "washington"):
            print ("Sorry i didn't understand you, could you repeat? \n ")
            continue
        else:
            break



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
       month= input ("What month do you want? Please enter a month of the year (jan-jun) or write all if you want data for all months available \n").lower()
       if month not in ("january", "february", "march", "april", "may", "june", "all"):
           print ("Sorry i didn't understand you, could you repeat? \n")
           continue
       else:
           break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day= input ("What day do you want? Please enter a day of the week or write all if you want data for everyday \n").lower()
       if day not in ("monday","tuesday","wednesday","thursday","friday","saturday","sunday", "all"):
           print ("Sorry i didn't understand you, could you repeat?")
           continue
       else:
           break

    print('-'*40)
    return city, month, day


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
    #I can take the function from previous exercises :

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month=df['month'].mode()[0]
    print('Most Common Month:', common_month)
    # TO DO: display the most common day of week

    common_day=df['day_of_week'].mode()[0]
    print('Most Common Day of the week:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('\n Most commonly used end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('\n Most  commonly used combination of start station and end station trip:', common_start_station, " & ", common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_time=sum(df['Trip Duration'])
    print('The travel duration was:', Total_time/86400, 'days') #the total time is in seconds, it is better to have it on days for the total duration

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('The mean of the trip duration was:', mean_time/60,'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types:', user_types )

#could get this part thanks to a post by khaledimad in github, since i wasn't able to remember myself the try except formula. I only got inspired by it for the try except part. The rest i wrote it myself.
    # TO DO: Display counts of gender
    try:
        gender_types=df['gender'].value_counts()
        print('Gender types:', gender_types )
    except KeyError:
        print("\n Gender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year )
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:', most_recent_year )
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', most_common_year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("Do you want to display raw data? Please answer yes or no\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':

            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows

            raw = input("Do you want to keep displaying raw data? Please answer yes or no\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5

        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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
	
print(city)
print(month)
