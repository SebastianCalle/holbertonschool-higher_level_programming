#include "lists.h"
/**
 * check_cycle - function that check if list has a cycle
 * @list: list to check
 * Return: 1 if has a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *aux1 = list;
	listint_t *aux2 = list->next;

	if (list == NULL)
		return (0);
	if (aux2 == aux1)
		return(1);
	while (aux2 != NULL)
	{
		aux1 = aux1->next;
		aux2 = aux2->next;
		if (aux2 != NULL)
			aux2 = aux2->next;
		else
			return (0);

		if (aux1 == aux2)
			return(1);
	}
	return (0);
}
