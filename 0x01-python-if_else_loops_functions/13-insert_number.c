#include "lists.h"
/**
 * insert_node - insert node
 * @head: head of list
 * @number: numbe rto ins
 * Return: NULL on fail addres of new node on succ
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	h = *head;
	if (h == NULL || h->n >= number)
	{
		new->next = h;
		*head = new;
		return (new);
	}

	while (h && h->next && h->next->n < number)
		h = h->next;
	
	new->next = h->next;
	h->next = new;
	return (new);
}
