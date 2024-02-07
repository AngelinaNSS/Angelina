# The Automation Project

In this file I will explain some of the commands I needed to use to create the project, and what they were used for:





1.
 <img width="301" alt="Screenshot 2024-02-07 at 04 26 20" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/429139ff-81c6-4553-b911-85cd52502de9">


This line imports the Tkinter module, which is a standard GUI (Graphical User Interface) toolkit for Python. It is commonly used for creating desktop applications with graphical interfaces. The as tk part gives Tkinter an alias tk, so you can refer to its classes and functions using tk instead of tkinter


2.
  <img width="337" alt="Screenshot 2024-02-07 at 04 26 24" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/0cf8e20c-7ab9-4c2d-b407-8edc84205791">

This line imports the messagebox module from Tkinter. The messagebox module provides a simple way to create and display message boxes in Tkinter applications. These message boxes can be used to show informational messages, warnings, errors

3.
    <img width="249" alt="Screenshot 2024-02-07 at 04 26 30" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/5aed4e34-d883-4b2c-8419-776de48b005c">

This line imports the schedule module. The schedule module is used for scheduling tasks to run at specific intervals or times. It provides a simple interface to create and manage scheduled tasks in Python programs.



4.
 <img width="252" alt="Screenshot 2024-02-07 at 04 26 36" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/222207c3-7aeb-4418-816e-0d19049d196d">

This line imports the built-in time module. The time module provides various time-related functions. It is commonly used for working with timestamps, measuring time intervals, and controlling program execution based on time.


5. 

<img width="186" alt="Screenshot 2024-02-07 at 04 29 16" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/1d81a7b1-1fc3-4b02-af2d-e97664162b6b">

The remind() function is a placeholder function definition. In Python, I learned that def is used to define a function. The function name in this case is 'remind.'


6.

<img width="454" alt="Screenshot 2024-02-07 at 04 31 47" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/3225e964-00ff-45ec-85a1-7f7b68af2e35">

This line of code schedules the remind() function to be executed every day at my desired time- 15:30PM. 

- schedule.every(): This is a method provided by the schedule module that initializes a scheduling job. It's the starting point for creating a schedule.
- .day: This specifies that the job should run every day.
- .at("15:30"): This specifies the time of day when the job should run, in this case, 15:30 or 3:30 PM.
- .do(remind): This specifies the function (remind) that should be executed when the scheduled time is reached.
So, altogether, this line sets up a recurring task using the schedule module, which will execute the remind() function every day at 15:30 for me.

7. 

<img width="415" alt="Screenshot 2024-02-07 at 04 35 31" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/ce521bac-cf94-4e5d-86ea-8f752077d11c">


This 'try' and 'except' statement is what I used for any error handling. It allowed me to write my code that might raise any problems, and to handle the exception, preventing the program from crashing, as well as to continue the execution of my program even if exceptions/problems do occur.

8.

<img width="414" alt="Screenshot 2024-02-07 at 04 37 53" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/dcfd40a1-c0d4-48c9-9a4b-3049dd96cba5">

The line print("Program stopped by user") is a simple print statement that outputs the message "Program stopped by user" to the console. For debugging or to track the flow of my execution. Printing a message like this would help me understand when and why my program was stopped during execution.

9. 


<img width="391" alt="Screenshot 2024-02-07 at 04 40 11" src="https://github.com/AngelinaNSS/Angelina/assets/148863357/67363ec6-bdda-41d9-8e1d-3239d580256c">


This code creates an infinite loop (while True:) that continuously checks for scheduled tasks and runs them using the schedule module.

-while True:: is an infinite loop that will run indefinitely because the condition True is always true. This loop ensures that the program keeps running continuously until it is manually stopped or interrupted.

-schedule.run_pending(): This line checks if there are any pending scheduled tasks and runs them. If there are no pending tasks, this function will do nothing and the loop continues to the next iteration.

-time.sleep(1): This line pauses the execution of the program for 1 second
This is done to prevent the loop from consuming excessive resources on my CPU by continuously checking for pending tasks. By sleeping for a short duration between iterations of the loop, the program can efficiently wait for scheduled tasks without using up all available processing power.





