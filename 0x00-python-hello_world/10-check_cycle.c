#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has 
 * cycle in it or not
 * @list: a ppinter to a linked list
 * Return: 0 if there is no cycle. 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *walking = list;
	listint_t *driving = list;

	if (!list)
		return (0);
	while (walking && driving && driving->next)
	{
		walking = walking->next;
		driving = driving->next->next;
		if (walking == driving)
			return (1);
	}
	return (0);
}
