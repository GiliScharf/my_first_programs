# This function gets a string of a date and it returns the day of the week
def date_to_weeks_day(date):
    from math import *
    month_dict={"march":1,"april":2,"may":3,"june":4,"july":5,"august":6,"september":7,"october":8,"november":9,"december":10,"january":11,"february":12}
    week_day_dict={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
    date_list=date.split()
    month=month_dict[date_list[0].lower()]
    century=int(date_list[2][0:2])
    year=int(date_list[2][2:4])
    if month>=11:
        year=year-1
    day=int(date_list[1])
    week_day=(day+floor(2.6*month-0.2)-2*century+year+floor(year/4)+floor(century/4))%7
    day_of_the_week=week_day_dict[week_day]
    return(day_of_the_week)