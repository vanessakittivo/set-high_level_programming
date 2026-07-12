#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints information about Python lists
 * @p: pointer to Python object
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    PyObject *item;
    Py_ssize_t i;

    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n",
           Py_SIZE(p));
    printf("[*] Allocated = %ld\n",
           list->allocated);

    for (i = 0; i < Py_SIZE(p); i++)
    {
        item = list->ob_item[i];
        printf("Element %ld: %s\n",
               i,
               Py_TYPE(item)->tp_name);
    }
}
