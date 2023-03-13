#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the pointer to first element in the list
 *
 * Return: 0 if it is not a palindrome or 1 if it is or -1 on error
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int length = 0, i = 0, *list;

	if (head != NULL)
	{
		if (*head == NULL)
			return (1);

		while (temp != NULL)
		{
			length++;
			temp = temp->next;
		}
		list = malloc(sizeof(int) * length);
		if (list == NULL)
			return (-1);

		temp = *head;
		while (temp != NULL)
		{
			list[i] = temp->n;
			temp = temp->next;
			i++;
		}
		for (i = 0; i < length / 2; i++)
		{
			if (list[i] != list[length - 1 - i])
			{
				free(list);
				return (0);
			}
		}
		free(list);
		return (1);
	}
	return (-1);
}
