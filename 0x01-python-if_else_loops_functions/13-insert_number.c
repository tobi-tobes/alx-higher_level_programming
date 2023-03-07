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
	listint_t *new_node, *temp;

	if (head != NULL)
	{
		temp = *head;
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		new_node->next = NULL;

		if (number < temp->n)
		{
			new_node->next = temp;
			temp = new_node;
			return (new_node);
		}
		while (temp && temp->next)
		{
			if (number > (temp->n) && number < (temp->next->n))
			{
				new_node->next = temp->next;
				temp->next = new_node;
				return (new_node);
			}
			temp = temp->next;
		}
		if (temp == NULL)
		{
			temp = new_node;
			return (new_node);
		}
	}
	return (NULL);
}
