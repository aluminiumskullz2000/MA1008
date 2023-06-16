date = input("Please input date in short format dd/mm/yyyy: ")
date1 = date.split("/")
month = {'1': "January", '2':'February','3':'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9':'September', '10':'October','11': 'November', '12': 'December'}
dates = [date1[0],month[date1[1]],date1[2]]

print (dates)

