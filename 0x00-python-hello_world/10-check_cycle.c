#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL)
		return (0);
	first = list;
	second = list;
	while (second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
