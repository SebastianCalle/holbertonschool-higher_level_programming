#include "lists.h"
/**
 * check_cycle - function that check if list has a cycle
 * @list: list to check
 * Return: 1 if has a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *aux1; 
	listint_t *aux2;

	if (!list)
		return (0);

	aux1 = list;
	aux2 = list->next;

	while (aux2 != NULL)
	{
		if (aux1 == aux2)
			return (1);
		aux1 = aux1->next;
		aux2 = aux2->next;
		if (aux2 != NULL)
			aux2 = aux2->next;
		else
			return (0);
	}
	return (0);
}
