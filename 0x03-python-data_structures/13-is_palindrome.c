#include "lists.h"
/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: list to check
 * Return: 0 if not a palindrome 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux, *aux2;
	int i, j;

	if (*head == NULL || head == NULL)
		return (0);
	aux = *head;
	for (i = 0; aux; i++, aux = aux->next)
		;
	aux2 = *head;
	while (i > 0)
	{
		for (j = 0, aux = *head; j < i - 1; aux = aux->next, j++)
			;
		if (aux->n != aux2->n)
			return (0);
		aux2 = aux2->next;
		i--;
	}
	return (1);
}

