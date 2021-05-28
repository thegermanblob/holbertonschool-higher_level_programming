#include "hash_tables.h"

/**
 * key_index - ets the index for the given key;
 * @key: key
 * @size: size of hash table
 * Return: index for hash table table
 *
 *
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
