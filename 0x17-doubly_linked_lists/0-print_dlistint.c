#include "lists.h"
/**
 * print_dlistint - prints a doubly linked list
 * @h: a pointer to the first node of the list
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *new;
	int count_nodes = 0;
	if (h == NULL)
		return (0);
	new = h;
	while (new != NULL)
	{
		printf("%d\n", new->n);
		new = new->next;
		count_nodes += 1;
	}
	return (count_nodes);
}
