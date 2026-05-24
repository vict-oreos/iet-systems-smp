# Task 1: : Monitor Active Internet Connections Using a Bash Script
- For this task, I first went through the basic commands used in the terminal and created a new directory using mkdir and then moved into that directory using cd.
- Following this, I created a new file explicitly using the touch command. I am aware that we can use nano directly but because I went step by step for the task, I created the file, then displayed its contents using the cat command, which showed that an empty file was created. Following this using the nano editor, I wrote the bash script.
- The first line is #!/bin/bash which is the shebang line that that basically tells the OS ie Linux, in this case that the file must be run using bash.
- Next, I have added the comment lines detailing what each columns displays in the output exactly.
- Then comes the most important part. As mentioned in the requirements of the task, I have neatly formatted the output. Using the ss -tunp command, the desired output is generated. I had read up on this command before. The ss command works as a Linux tool to show the device's active internet connections and -tunp narrows it down to the UDP and TCP connections that are required to be displayed along with their process ie which program is using these connections.
- Finally, I saved and exited the nano editor using CTRL+S and CTRl+X and then executed the bash script using chmod +x and then i ran the program using ./

