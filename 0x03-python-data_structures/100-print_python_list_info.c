#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
#define _POSIX_C_SOURCE 200809L

/**
 * print_python_list_info - prints a python list info
 * @p: a pointer to a python nobject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyTypeObject *type;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(obj->ob_item[i]);
		printf("Element %d: %s\n", i, type->tp_name);
	}
}
