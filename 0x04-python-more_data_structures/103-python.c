#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: Python object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;
	const char *type;

	type = p->ob_type->tp_name;
	printf("[.] bytes object info\n");
	if (strcmp(type, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", (size < 10 ? size + 1 : 10));
	for (i = 0; i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i == size || i == 9)
			break;
		printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists.
 * @p: Python object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocd, i;
	PyObject *item;
	const char *type;

	size = PyList_Size(p);
	allocd = ((PyListObject *)(p))->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocd);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}
