import webbrowser
import time

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=guKoNCQFAFk&list=PLjzeyhEA84sQKuXp-rpM1dFuL2aQM_a3S")
    break_count = break_count + 1

