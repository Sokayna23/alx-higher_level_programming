#include "lists.h"

/**
 * is_palindrome - chacks wether a singly linked list is a palindrome
 * @head: a pointr to a pointer to the first element of the list
 * Return: 0 if it is not palindrome, or 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *end = *head;
	int nodes = 0, i = 0, j = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (start)
	{
		start = start->next;
		nodes++;
	}
	start = *head;
	for (i = 1; i <= nodes; i++)
	{
		for (j = i; j <= nodes - i; j++)
			end = end->next;
		if (start->n != end->n)
			return (0);
		start = start->next;
		end = start;
	}
	return (1);
}
