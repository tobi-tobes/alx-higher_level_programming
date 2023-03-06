#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to first item in singly-linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (list != NULL)
	{
		while (slow && fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;

			if (fast == slow)
				return (1);
		}
	}
	return (0);
}
