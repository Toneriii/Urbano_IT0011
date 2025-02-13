months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

date_input = input("Enter the date (mm/dd/yyyy): ")

try:

    month, day, year = date_input.split("/")
    
    day = str(int(day))
    
    if month in months:
        formatted_date = f"{months[month]} {day}, {year}"
        print(f"Date Output: {formatted_date}")
    else:
        print("Invalid month entered")
        
except:
    print("Invalid date format. Please use mm/dd/yyyy")
