# Automation work, previously using ubuntu 


My Automation Project: A Notification to remind me to take my vitamins! (at a certain time during the day.)

Problem and Context of the Automation:
To begin the "Creating a reminder system on Ubuntu," I use a combination of a command-line tool on Ubuntu and the ssh command to trigger a notification, to notify me on my Mac.

<img width="392" alt="Screenshot 2024-02-02 at 15 06 52" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/2369023d-0b68-450d-8f9c-57767fcdaf47">

For the next process I needed to "Create a script for the reminder": The script i chose was called "vitamin_reminder.sh" using a text editor:


<img width="389" alt="Screenshot 2024-02-02 at 15 09 01" 
src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/71adc6b7-4309-470b-8adc-0e40de7dbfbe">



Next I used "osascript" on macOS, it is a command-line tool that allows you to run AppleScript commands from the terminal.



<img width="503" alt="Screenshot 2024-02-02 at 18 48 48" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/bfc98a48-820e-47ad-b4b9-4b466fecf45e">



<img width="513" alt="Screenshot 2024-02-02 at 18 49 02" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/7d9aaffb-7fa5-4e04-b2b4-192b7d52



To Make the script executable:



<img width="412" alt="Screenshot 2024-02-02 at 18 50 31" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/e5e89f56-5efd-4406-9a6a-ac195381f617">



Lastly I used the "at" command to Schedule the reminder and to schedule the script to run at a specific time:

I had to manually install the command "at" on to my ubuntu using: "sudo apt-get install at" on my Terminal. This command allows you to schedule a one-time job to be executed at a specific time in the future. In case, I wanted to schedule my vitamin reminder script to run at a specific time.

<img width="477" alt="Screenshot 2024-02-02 at 18 51 44" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/6a5d58cf-86a1-4369-97f6-d1fc151a74e8">


The Time I set it to was 15:30🕞 every day!




To make sure that my automation was running properly, there were three ways that I used to check:

The first way was to wait for the Time: 15:30 for a notification to pop up on my screen.

The second was to check, I opened Terminal on my Ubuntu and typed the command 'atq'to "view scheduled jobs" for the day. Just like the 'at' command, I also had to manually install this: for which I used the command -

<img width="396" alt="Screenshot 2024-02-02 at 19 22 54" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/edcf4281-84e4-43be-9fd1-f7fac084b2c6">

This 'atq' command displayed the job numbers and the times they are scheduled to run. Since my vitamin reminder was scheduled, I was able to see it in the list.

The Third way I could Manually Trigger the Reminder:
I wanted to quickly test my script without waiting for the scheduled time, so I learned how to execute it manually. I went to the script's directory and typed the command:


<img width="424" alt="Screenshot 2024-02-02 at 19 21 41" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/f66b2f96-165c-487b-bb04-74f3d68f7714">


I did encounter several problems along the way. Many times when i tried to execute a certain command, I had recieved alot of "Syntax Error" while trying to run the script.
So I had to go back many times and check any mistakes I have made. I had to check for Errors in the message, and review the script. 
Also when I was checking to see if the project was working and I typed the "at" command, it showed me a pop up that said "Garbled Time" indicating that something was wrong, so I also had to research ways to avoid this. The "garbled time" error with the "at" command occurs when there's an issue with the time format tha I was providing. The "at" command needs the time to be specified in a specific format in order to work. In Ubuntu, the time format should be in HH:MM (24-hour clock), which is a mistake I made in the beginning not using 24 hour time format. I had to make sure my Ubuntu system was up to date, so I used the command "sudo apt-get update" and "sudo apt-get upgrade." Another problem I ran in to was connecting my work on Ubuntu to my mac. To do this I had to Enable "SSH" on Ubuntu. To make sure my Ubuntu machine had the SSH server installed and running following command:



<img width="370" alt="Screenshot 2024-02-03 at 13 53 09" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/a0d974ef-aeaa-4e51-a172-7a62459a5a7c">





<img width="347" alt="Screenshot 2024-02-03 at 13 53 14" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/3e4945bd-875a-46d8-aa8c-2eee154f3388">




Next was a very Important step with connecting my mac with ubuntu. I learned about a website cal "Todoist.com." With this website I made an account, and also made an account through Ubuntu. I was able to connect and sync both devices together, so that whatever I do on my mac, also happens on my ubuntu software, and vice versa.

<img width="344" alt="Screenshot 2024-02-04 at 18 59 06" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/51980e60-da43-4deb-bdd7-ac5eafcfaec6">


The photo above is a screenshot of my mac in the process of connecting my ubuntu automation, to my regular desktop.

I also wanted to connect the reminder to a sound, or a chime. So I not only see the message, "take your vitamins" but also to hear it. I was able to add the sound by using the terminal on my ubuntu. I used the following commands:


<img width="548" alt="Screenshot 2024-02-04 at 18 32 37" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/330524c5-3835-4e29-b28d-547bb72044a4">


The "paplay" I had to install in order to start choosing what sound I want to hear. While adjusting the sound settings on my terminal to make it audible.


<img width="422" alt="Screenshot 2024-02-04 at 17 31 53" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/768b424d-14d5-48c3-aa2f-9b6b68759111">



And lastly I wanted to make sure that my automation was able to run automatically everyday at the same time. After searching online, I found a command called "cron." This enabled me to have the reminder message pop up automatically every day at the same time. 'cron' allows you to schedule tasks at predefined times. The command I used: crontab -e. And I had to find a command to let me adjust the time that I wanted the chime to go off, so I used the command "echo."


<img width="519" alt="Screenshot 2024-02-04 at 18 27 53" 
src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/4e0d80c1-0f65-4624-9f5c-86a4d8ede6d5">


<img width="261" alt="Screenshot 2024-02-04 at 18 27 57" src="https://github.com/AngelinaNSS/AngelinaNSS/assets/148863357/f2704f98-c5bf-4fc8-8b9c-335bfdde5f21">

