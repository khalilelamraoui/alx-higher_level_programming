#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *second_half, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev_slow;
		prev_slow = temp;
	}
	if (fast != NULL)
		slow = slow->next;
	second_half = slow;
	while (prev_slow != NULL && second_half != NULL)
	{
		if (prev_slow->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		prev_slow = prev_slow->next;
		second_half = second_half->next;
	}
	prev_slow = NULL;
	while (*head != NULL)
	{
		temp = *head;
		*head = (*head)->next;
		temp->next = prev_slow;
		prev_slow = temp;
    	}
	return is_palindrome;
}
