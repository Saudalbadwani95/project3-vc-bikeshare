import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters_and_laod_data():
    """
    Asks user to specify a city, month, and day to analyze.
    Then loads the data for the entered inputs and dealing with NaN values

    finally return the dataframe (df)

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while city not in CITY_DATA.keys():
        # the while loop will keep looping and ask the user for input ...
        # ... if the input (city) doesn't match any of the key in the (CITY_DATA) dictionary
        city = input("enter city name from the following (chicago, new york city, washington) : ").lower()
        continue
    else:
        # if the input match a key in the (CITY_DATA) dictionary
        print('-'*40, ' The city is set as: ', city)

    df = pd.read_csv(CITY_DATA[city]) # takes the data from csv file of the input (city)

    # Dealing with NaN value
    df = df.fillna(method = 'ffill', axis = 0)


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    month = None
    while month not in months:
        # the while loop will keep looping and ask the user for input ...
        # ... if the input (month) doesn't match any of the values in the (months) list
        month = input("Enter the month name from the following (january, february, ... , june) or if you want to show all the months please enther all : ").lower()
        continue
    else:
        # if the input match a value in the (months) list
        if month == 'all':
            # if the user chose 'all' then return the month column of the month with no changes
            df['month'] = df['month']
        else:
            # if the user chose different value for (months) list other than 'all'

            print('-'*40, 'The month is set as: ', month) # display the month

            df = df[df['month'] == month.title()] # filter by month to create the new dataframe

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayofweek = ['all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    day = None
    while day not in dayofweek:
        # the while loop will keep looping and ask the user for input ...
        # ... if the input (day) doesn't match any of the values in the (dayofweek) list
        day = input("Enter the day name from the following (monday, tuesday, ... sunday) or if you want to show all the days please enther all :  ").lower()
        continue
    else:
        # if the input match a value in the (dayofweek) list
        if day == 'all':
            # if the user chose 'all' then return the day_of_week column with no changes
            df['day_of_week'] = df['day_of_week']
        else:
            # if the user chose different value from (dayofweek) list other than 'all'
            print('-'*40, "The day is set as: ", day)

            df = df[df['day_of_week'] == day.title()] # filter by day of week to create the new dataframe


    print('-'*40)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month']
    print("Common month is", popular_month.mode()[0]) # take the mode value and display the most common month

    # TO DO: display the most common day of week
    popular_day = df['day_of_week']
    print("Common day is ", popular_day.mode()[0]) # take the mode value and display the most common day

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common start hour
    popular_hour = df['hour']
    print('Common Start Hour:', popular_hour.mode()[0])  # take the mode value and display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station']
    print('Most common start statin: \n ', popular_start_station.mode()[0]) # take the mode value and display commonly used start station

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station']
    print('Most common end station: \n ', popular_end_station.mode()[0]) # take the mode value and display commonly used end station

    # TO DO: display most frequent combination of start station and end station trip

    # Adding the start station column and end station column together
    popular_combination_station = ("Start station: " + df['Start Station'] + " || End station: " + df['End Station'])
    # takes the mode value and display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip \n  ', popular_combination_station.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time_sec = sum(df['Trip Duration']) # taking the sum of Trip Duration column
    as_hours = (total_travel_time_sec/3600).__round__(0) # changing from second to hours
    as_day = (as_hours/24).__round__(0) # changing from hours to days
    print('Total travel time: ',as_hours , ' Hours or ', as_day, 'days') # Display the total travel time

    # TO DO: display mean travel time

    avarge_travel_time_seco = (df['Trip Duration']).mean() # taking the mean of Trip Duration column
    ave_time_hr = (avarge_travel_time_seco/3600).__round__(1) # changing from second to hours
    print('Average travel time: ', ave_time_hr ,'Hours') # Display the mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    subscriber_count = [ x for x in df['User Type'] if x == 'Subscriber'] # taking only the Subscriber from User Type column
    print("Count of", pd.value_counts(subscriber_count)) # counting the number of Subscriber and display the count
    customer_count = [ x for x in df['User Type'] if x == 'Customer'] # taking only the Customer from User Type column
    print("Count of", pd.value_counts(customer_count)) # counting the number of Customer and display the count

    # TO DO: Display counts of gender

    try:
        male_count = [x for x in df['Gender'] if x == 'Male'] # taking only the Male from Gender column
        print("Count of", pd.value_counts(male_count)) # counting the number of Male and display the count
        female_count = [x for x in df['Gender'] if x == 'Female'] # taking only the Female from Gender column
        print("Counts of", pd.value_counts(female_count)) # counting the number of Female and display the count

    except KeyError: # this except statement for handling the error generate from Washington data
        print("NOTE: The data file dose not contain gender information")
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_bd = df['Birth Year'].min() # takes the earliest birth year by taking the min value in Birth year column
        print("Earliest year of birth is: ", earliest_bd) # Display the earliest birth year
        recent_bd = df['Birth Year'].max() # takes the recent birth year by taking the max value in Birth year column
        print("Recent year of birth is", recent_bd) # Display the recent birth year
        common_bd = df['Birth Year']
        print("Common year of birth is", common_bd.mode()[0]) # takes the common birth year by taking the mode value and display it

    except KeyError: # this except statement for handling the error generate from Washington data
        print("NOTE: The data file dose not contain year of birth information")
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        df = get_filters_and_laod_data()


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        ''' the loop is asking if the user want to see raw data 
            if the user type yes it wll shows 5 rows of data 
            if the user type yes again it will shows the next 
            it the user type no it will exit the loop'''
        n = 0
        while (n < df.shape[0]):
            raw_data = input("would you like to see raw data ? Enter yes or no: ").lower()
            if raw_data == 'yes':
                print(df.iloc[n:n+5])
                n += 5

            elif raw_data == 'no':
                break
        pass

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
