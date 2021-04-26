#include "lists.h"
/**
  * check_cycle - check for loop
  *@list: the list being checked
  *Return: 0 on true of 1 on loop found
  */
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	node1 = list;
	if (list == NULL)
		return (0);
	node2 = list->next;
	while (node2 != NULL && node2->next != NULL && node1 != NULL)
	{
		if (node1 == node2)
			return (1);
		node1 = node1->next;
		node2 = node2->next->next;
	}
	return (0);
}
