#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert node for number
 * @head: list head
 * @number: number to insert
 * Return: null if not succes or new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux1, *aux2, *new;

	new = malloc(sizeof(int));
	if (new == NULL)
		return (NULL);
	aux1 = *head;
	aux2 = aux1->next;
	if (head == NULL)
	{
		new->n = number;
		aux1->next = new;
		new->next = aux2;
		return (new);
	}


	while (aux2 != NULL)
	{
		if (aux1->n < number && aux2->n > number)
		{
			new->n = number;
			aux1->next = new;
			new->next = aux2;
			return (new);
		}
		aux1 = aux1->next;
		aux2 = aux2->next;
	}
	return (NULL);
}
