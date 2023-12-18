#include<stdio.h>
#include<stdlib.h>
#include<Python.h>
#include<listobject.h>
#include<floatobject.h>
#include<bytesobject.h>
#include<float.h>

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
	Py_ssize_t i, size;
	PyObject *item;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, item->ob_type->tp_name);
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
* print_python_bytes - prints some basic info about Python bytes
* @p: pointer to PyObject
* Return: void
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %ld\n", size);
		str = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", str);
		if (size < 10)
			printf("  first %ld bytes:", size + 1);
		else
			printf("  first 10 bytes:");
		for (i = 0; i <= size && i < 10; i++)
			printf(" %02x", str[i] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
* print_python_float - prints some basic info about Python float
* @p: pointer to PyObject
* Return: void
*/
void print_python_float(PyObject *p)
{
	char *str;

	double d;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		d = ((PyFloatObject *)p)->ob_fval;
		str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", str);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}
