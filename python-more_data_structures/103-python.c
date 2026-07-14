#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints Python bytes object info
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, limit;
	char *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	limit = size + 1;
	if (limit > 10)
		limit = 10;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)bytes[i]);

	printf("\n");
}

/**
 * print_python_list - prints Python list information
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *list;
	PyObject *item;

	if (!PyList_Check(p))
		return;

	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n",
	       PyList_Size(p));
	printf("[*] Allocated = %ld\n",
	       list->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n",
		       i,
		       Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
