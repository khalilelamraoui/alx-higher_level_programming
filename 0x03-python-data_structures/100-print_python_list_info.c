#include <Python.h>
#include <stdio.h>
#include <listobject.h>
/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to the Python list
 *
 * This function retrieves the size and allocated space of the Python list
 * and prints the information. It also iterates through the list elements,
 * printing the type of each element.
 */
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int counter;
	PyObject *object;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)list->allocated);
	for (counter = 0; counter < size; counter++)
	{
		object = PyList_GetItem(p, counter);
		printf("Element %d: %s\n", counter, Py_TYPE(object)->tp_name);
	}
}