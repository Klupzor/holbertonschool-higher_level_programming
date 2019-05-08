#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - evaluate int list
 * @head: head of list
 * Return: 1 if is and 0 if not
 */

int is_palindrome(listint_t **head)
{
	int nums[10000];
	int size = 0;
	int in, fin;
	listint_t *tmp;

	tmp = *head;

	while (tmp)
	{
		nums[size] = tmp->n;
		tmp = tmp->next;
		size++;
	}
	size--;
	for (in = 0, fin = size ; in < size / 2 ; in++, fin--)
	{
		if (nums[in] != nums[fin])
			return (0);
	}
	return (1);
}
