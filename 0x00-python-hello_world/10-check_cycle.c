#include "lists.h"
/**
 * check_cycle - checks to see if there is cycle in list
 * @list: list to check
 * Return: 0 if no cylce 1 if cyclce
 */
int check_cycle(listint_t *list)
{
	size_t array[1000];
	int j, i = 0;

	while (list->next)
	{
		array[i] = (size_t)list;
		for (j = 0; j < i; j++)
		{
			if(array[j] == (size_t)list)
				return (1);
		}
		list = list ->next;
		i++;
	}
	return (0);
}


