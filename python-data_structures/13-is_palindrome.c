#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: head of list
 *
 * Return: new head
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

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
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head pointer
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *second, *copy_second;
	listint_t *first;
	int palindrome = 1;

	if (head == NULL || *head == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second = reverse_list(slow);
	copy_second = second;
	first = *head;

	while (second)
	{
		if (first->n != second->n)
		{
			palindrome = 0;
			break;
		}

		first = first->next;
		second = second->next;
	}

	reverse_list(copy_second);

	return (palindrome);
}
