# Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = 11, 12, 2014
# Sample Output : The examination will start from : 11 / 12 / 2014
print("Input a date time sample as 11,12,20014")
seq = input()
print("Date time is: ", seq.replace(",","/"))