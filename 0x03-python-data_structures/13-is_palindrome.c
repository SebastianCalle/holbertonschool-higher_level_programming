#include "lists.h"
/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: list to check
 * Return: 0 if not a palindrome 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux;
	int i, j[10000];

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	aux = *head;
	for (i = 0; aux; i++, aux = aux->next)
		j[i] = aux->n;
	aux = *head;
	while (i > 0)
	{
		if (aux->n != j[i - 1])
			return (0);
		aux = aux->next;
		i--;
	}
	return (1);
}

