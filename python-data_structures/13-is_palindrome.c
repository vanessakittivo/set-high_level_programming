#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head
 * Return: new head
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next;

	while (head)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if linked list is palindrome
 * @head: pointer to pointer to head
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second;

	if (head == NULL || *head == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second = reverse_list(slow);

	while (second)
	{
		if ((*head)->n != second->n)
			return (0);
		*head = (*head)->next;
		second = second->next;
	}

	return (1);
}
