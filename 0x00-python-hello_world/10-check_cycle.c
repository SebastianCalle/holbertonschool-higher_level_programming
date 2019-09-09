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

	while (aux1 != NULL)
	{
		while(aux2)
		{
			if (aux2 == aux1)
				return (1);
			else if (aux2 == NULL)
				return(0);
			aux2 = aux2->next;

		}
		aux1 = aux1->next;
	}
	return (0);
}
