#include "lists.h"
/**
 * check_cycle - checks to see if there is cycle in list
 * @list: list to check
 * Return: 0 if no cylce 1 if cyclce
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list->next;

	while(list->next)
	{
		if (list == tmp)
			return (1);
		list = list->next;
		if (tmp->next)
			tmp = tmp->next;
		if (tmp->next)
			tmp = tmp->next;
	}
	return(0);
}

