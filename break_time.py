import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=k2JRdHKS-Zw")
    total_breaks = total_breaks + 1
