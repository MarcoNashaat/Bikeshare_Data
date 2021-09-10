#importing necessary libraries.
import pandas as pd
import numpy 
def calculations(target,month=None,day=None):
    """
    takes three arguments: *target(city to make calculations on) and it's requried.
                           *month and day(to filter data) and it's optional.
    returns some calculations based on the dataset and the filters applied if there's any.
    """
    df = pd.read_csv(target)
    df.dropna(inplace=True)                               #droping all NAN values.
    df['Start Time'] = pd.to_datetime(df['Start Time'])   #making sure time and date are in correct format.

    #extracing month, day, hour, and trips.
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    df['trips'] = df['Start Station'] + ',' + df['End Station']
    # print(df)


    #checking if month and day are specified, so not to return common 
    #day and month(unnecessary data).
    if month != None:
        months = ['janurary', 'february', 'march', 'april', 'may', 'june']
        df=df[df['month'] == months.index(month)+1]
        # print(df)                 
    else:
        months = ['janurary', 'february', 'march', 'april', 'may', 'june']
        print('most common months: {}'.format(months[df['month'].mode()[0]-1]))
    if day != None:
        days = ['monday','tuesday','wednsday','turesday','friday','saturday','sunday']
        df=df[df['day'] == days.index(day)]
        # print(df)
    else:
        days = ['monday','tuesday','wednsday','turesday','friday','saturday','sunday']
        print('most common day: {}'.format(days[df['day'].mode()[0]-1]))
    

    #common hour.
    hours = numpy.arange(24)
    print('most common hour: {}\n'.format(hours[df['hour'].mode()[0]]))

    #common start station, end station, and trip.
    print('most common start station: {}'.format(df['Start Station'].mode()[0]))
    print('most common end station: {}'.format(df['End Station'].mode()[0]))
    print('most common trip: {}\n'.format(df['trips'].mode()[0]))

    #total and average trip duration.
    print('total travel time(in hours): {}'.format(round(df['Trip Duration'].sum()/3600,2)))
    print('average travel time(in minutes): {}\n'.format(round(df['Trip Duration'].mean()/60,4)))

    #count and percentage of user type.
    print('count of user types:\n{}'.format(df['User Type'].value_counts()))
    print('with percentage of:\n{}'.format(df['User Type'].value_counts(normalize=True)))

    
    if target == 'new_york_city.csv' or target == 'chicago.csv':    #making sure the user picked a city with enough data
        #count and percentage of each gender.
        print('count of each gender:\n{}'.format(df['Gender'].value_counts()))
        print('with percentage of"\n{}\n'.format(df['Gender'].value_counts(normalize=True)))
        #oldest and youngest and mean birth of year.
        print('earliest year of birth is: {}'.format(int(df['Birth Year'].min())))
        print('most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
        print('most common year of birth is: {}'.format(int(df['Birth Year'].mode()[0])))
    i=0
    #looping through the whole dataset or till the user hit no.
    while input("would you like to show full data?[y/n]") in'Yy' and i < len(df):
        print(df.iloc[i:i+5])
        i+=5


def option_day():
    """
     function that prompts the user to pick a day.
     doesn't take any arguments.
     return the day entered by user if there's any.
    """
    option_day_=input("would you like to filter data by day?[y/n]")
    if option_day_.lower() == 'y':
        days = ['monday','tuesday','wednsday','turesday','friday','saturday','sunday']
        day = str(input("pick a day['monday','tuesday','wednsday','turesday','friday','saturday','sunday']\n"))
        if day.lower() in days:            #checking if the input is valid and then returning it.
            return day
        else:
            print('invalid input, try again')       #rejecting invalid input.
            option_day()     #recursivly calling the function again.
    elif option_day_.lower() == 'n':
        return None                #returning none when user picks no.       
    else:
        print("invalid input, try again")     #rejecting invalid input.
        option_day()       #recursivly calling the function again.

def option_month():
    """
     function that prompts the user to pick a month.
     doesn't take any arguments.
     return the month entered by user if there's any.
    """
    option_month_=input("would you like to filter data by month?[y/n]")
    if option_month_ == 'y' or option_month_ == 'Y':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = str(input("pick a month['january', 'february', 'march', 'april', 'may', 'june']\n"))
        if month.lower() in months:          #checking if the input is valid and then returning it.
            return month
        else:
            print('invalid input, try again')          #rejecting invalid input.
            option_month()         #recursivly calling the function again.
    elif option_month_ == 'n' or option_month_ == 'N':
        return None        #returning none when user picks no.
    else:
        print("invalid input, try again")      #rejecting invalid input.
        option_month()      #recursivly calling the function again.

def cities():
    """
     function that prompt the user to pick a city and reject any invalid inputs.
     takes no arguments.
     returns the appropriate file.
    """
    cities_dict={'chicago':'chicago.csv',            
            'newyork':'new_york_city.csv',
            'washington':'washington.csv'}
    target=input("pick from avalible cities[chicago, newyork, Washington] \n")
    if target.isalpha()==False or target.lower() not in cities_dict:   #rejecting non alphaptical inputs and non existing cities.
        print('please enter valid city name')
        cities()    #recursivly calling the function when input is invalid.
    else:
        target=cities_dict[target.lower()]   #getting file name
        calculations(target,option_month(),option_day())   


def wrap_function():
    print("Ready for some data?!")
    cities()
    while input("Ready to go again?[y/n]") in'Yy':   #restarting the program everytime the answers yes.
        cities()

wrap_function()