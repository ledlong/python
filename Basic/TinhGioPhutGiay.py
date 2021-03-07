try:
    # Nhap vao so giay t bat ky
    t = int(input("Nhap vao so giay bat ky: "))
    if t >= 0:
        hour = (t // 3600) % 24
        minute = (t % 3600) // 60
        second = (t % 3600) % 60
        print(hour, ":", minute, ":", second)
    else:
        print("Second is negative")
except:
    print("Error happens")
print("Thank you for using the app")
