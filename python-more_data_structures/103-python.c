#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_bytes - prints Python bytes object info
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size, i, limit;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = bytes->ob_base.ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	limit = size + 1;
	if (limit > 10)
		limit = 10;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)bytes->ob_sval[i]);

	printf("\n");
}

/**
 * print_python_list - prints Python list information
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject **items;
	Py_ssize_t i;

	if (!PyList_Check(p))
		return;

	list = (PyListObject *)p;
	items = list->ob_item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n",
	       list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n",
	       list->allocated);

	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %ld: %s\n",
		       i,
		       items[i]->ob_type->tp_name);

		if (PyBytes_Check(items[i]))
			print_python_bytes(items[i]);
	}
}
