#include<stdio.h>
#include<unistd.h>
int main(){
	printf("Process ID (PID) is %d",getpid());
	printf("\n");
	fflush(stdout);
	sleep(60);
	return 0;
}
