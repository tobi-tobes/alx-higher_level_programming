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
	listint_t *new_node, *temp, *prev;

	if (head != NULL)
	{
		temp = *head;
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;

		while (temp && number > (temp->n)))
		{
			prev = temp;
			temp = temp->next;
		}
		new_node->next = temp;

		if (prev != NULL)
			prev->next = new_node;
		else
			*head = new_node;
		return(new_node);
	}
	return (NULL);
}
