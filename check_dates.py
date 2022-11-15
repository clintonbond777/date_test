from lunarcalendar import \
    Converter, \
    Lunar, \
    Solar, \
    DateNotExist 

import pandas as pd
from datetime import date

start_date = date(2024,7,1)
end_date = date(2025,1,31)


def date_to_lunar(date_str):
        try:
            val = Lunar.from_date(date_str)
            val = date(val.year, val.month, val.day) #extract out without conversion to solar method

        except DateNotExist:
            val = pd.NA
        
        return val

def contains_8(date_str):
    
    if '8' in str(date_str.month) or '8' in str(date_str.day):
        return True
    else:
        return False


def make_dates(start_date, end_date):
    daterange = pd.date_range(start_date, end_date)

    # print(daterange)

    df = pd.DataFrame({'greg_date': daterange})

    df['day_of_week'] = df.greg_date.dt.day_of_week

    

    df['lunar'] = df['greg_date'].apply(func = date_to_lunar)

    df['contains_8_greg'] = df['greg_date'].apply(func = contains_8)
    df['contains_8_lunar'] = df['lunar'].apply(func = contains_8)
    pd.set_option('display.max_rows', None)


    df = df[
            (df['day_of_week']==5) &
            (df['contains_8_greg'] ==True) &
            (df['contains_8_lunar'] ==True)
        ]
    return df

if __name__ == '__main__':
    start_date = date(2024,7,1)
    end_date = date(2025,1,31)
    print(make_dates(start_date, end_date))






