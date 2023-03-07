#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly-linked list
 * @head: pointer to the pointer to first element in the list
 * @number: number to be added into list
 *
 * Return: pointer to new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	if (head != NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		new_node->next = NULL;

		if (number < *head->n)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
		else
		{
			while (*head && *head->next)
			{
				if (number > *head->n && number < *head->next->n)
				{
					new_node->next = *head->next;
					*head->next = new_node;
					return (new_node);
				}
				*head = *head->next;
			}
			if (*head == NULL)
			{
				*head = new_node;
				return (new_node);
			}
		}
	}
	return (NULL);
}
