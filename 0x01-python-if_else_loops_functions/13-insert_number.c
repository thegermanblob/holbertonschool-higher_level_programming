#include "lists.h"
/**
 * insert_node - insert node
 * @head: head of list
 * @number: numbe rto ins
 * Return: NULL on fail addres of new node on succ
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h, *tmp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	h = *head;
	tmp = *head;
	tmp = tmp->next;
	if (head == NULL)
	{
		new->next = NULL;
		return (NULL);
	}

	while (h != NULL)
	{
		if ((tmp->n >= number) || (h->next == NULL))
		{
			h->next = new;
			new->next = tmp;
			break;
		}

		h = h->next;
		tmp = tmp->next;
	}
	return (new);
}
