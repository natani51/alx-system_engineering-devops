#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - creates an infinite loop
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombies process
 * Return: 0
 *
 */
int main(void)
{
	int z;
	pid_t zombie;

	for (z = 0; z < 5; z++)
	{
		zombie = fork();
		if (zombie == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
