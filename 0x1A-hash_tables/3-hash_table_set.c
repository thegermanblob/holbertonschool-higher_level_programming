#include "hash_tables.h"

/**
 * hash_table_set - sets a key val pair in the hash table
 * @ht: hash table
 * @key: key
 * @value: value
 *
 * Return: 0 fail 1 succ
 *
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{

	hash_node_t *node;
	char *val;
	unsigned long int index, i;

	if (ht == NULL || key == NULL || *key == '\0' || value == NULL)
		return (0);
	val = strdup(value);
	if (!val)
		return (0);
	index = key_index((const unsigned char *)key, ht->size);
	for (i = index; ht->array[i]; i++)
	{
		if (strcmp(ht->array[i]->key, key) == 0)
		{
			free(ht->array[i]->value);
			ht->array[i]->value = val;
			return (1);
		}
	}
	node = malloc(sizeof(hash_node_t));
	if (!node)
	{
		free(val);
		return (0);
	}
	node->key = strdup(key);
	if (!node->key)
	{
		free(node);
		return (0);
	}
	node->value = val;
	node->next = ht->array[index];
	ht->array[index] = node;
	return (1);
}
