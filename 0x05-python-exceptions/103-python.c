#include<stdio.h>
#include<stdlib.h>
#include<Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_list - prints some basic info about Python lists
* @p: pointer to PyObject
* Return: void
*/
void print_python_list(PyObject *p)
{
	int counter, size;
	PyObject *item;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
		for (counter = 0; counter < size; counter++)
		{
			item = PyList_GetItem(p, counter);
			printf("Element %d: %s\n", counter, Py_TYPE(item)->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
/**
* print_python_bytes - prints some basic info about Python lists
* @p: pointer to PyObject
* Return: void
*/
void print_python_bytes(PyObject *p)
{
	int counter, size;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %d\n", size);
		str = PyBytes_AsString(p);
		printf("  trying string: %s\n", str);
		if (size < 10)
			printf("  first %d bytes:", size + 1);
		else
			printf("  first 10 bytes:");
		for (counter = 0; counter <= size && counter < 10; counter++)
			printf(" %02hhx", str[counter]);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
/**
* print_python_float - prints some basic info about Python lists
* @p: pointer to PyObject
* Return: void
*/
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (PyFloat_Check(p))
		printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
	else
		printf("  [ERROR] Invalid Float Object\n");
}
