#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_float - prints some basic info about Python floats
 * @p: Python object
 * Return: Nothing
 */
void print_python_float(PyObject *p)
{
	double value;
	const char *type;

	type = p->ob_type->tp_name;
	printf("[.] float object info\n");
	if (strcmp(type, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	if ((int) value == value)
		printf("  value: %0.1f\n", value);
	else
		printf("  value: %0.16g\n", value);
	fflush(stdout);
}

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
	str = ((PyBytesObject *)p)->ob_sval;

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
	fflush(stdout);
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
	const char *type, *check;

	printf("[*] Python list info\n");
	check = p->ob_type->tp_name;
	if (strcmp(check, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocd = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocd);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(type, "float") == 0)
			print_python_float(item);
	}
	fflush(stdout);
}
