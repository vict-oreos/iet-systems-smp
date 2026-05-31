# Task 2: Linux Syscalls and strace Assignment
- For this task, I initially executed the commands in the terminal namely, strace ls. This produced a long output including numerous types of syscalls ie system calls. These are detailed with the parameters mentioned inside as well.
- I then read up on each one of these and what a syscall is. Following this, I also read up on the paramteres present in each of these like fd which refers to the file descriptor.
- After this, I then executed strace -e openat ls which displays only openat syscalls by filtering through the output due to the excption -e added.
- After, I created answers.txt directly using nano command in the terminal. I displayed its contents initially to show it was empty using cat command. Follwoing this, I began to edit the file and answer the questions given
- I went in the order of the syscalls that were displayed when i received the output for strace ls to answer the second question. After editing, I saved ande exited using CTRL+S and CTRL+X.
- Finally, I displayed the contents of the file in the terminal as well.
