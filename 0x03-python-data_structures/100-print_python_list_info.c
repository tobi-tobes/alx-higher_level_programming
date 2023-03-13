#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocd, i;
	PyObject *item;
	const char *type;

	size = PyList_size(p);
	allocd = ((PyListObject *)(p))->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocd);


	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
