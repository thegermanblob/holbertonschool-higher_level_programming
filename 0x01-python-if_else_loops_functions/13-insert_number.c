#include "lists.h"
/**
 * insert_node - insert node
 * @head: head of list
 * @number: numbe rto ins
 * Return: NULL on fail addres of new node on succ
 */
listint_t *insert_node(listint_t **head, int number)
{
	int j, i = 0;
	listint_t *h, *tmp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return(NULL);
	new->n = number;
	h = *head;
	tmp = *head;
	tmp = tmp->next;
	if (head == NULL)
	{
		return(NULL);
	}

	while (h != NULL)
	{
		if (tmp->n > number)
		{
			h->next = new;
			new->next = tmp;
			break;
		}

		i++;
		h = h->next;
		tmp = tmp->next;
	}
	return(new);
}
