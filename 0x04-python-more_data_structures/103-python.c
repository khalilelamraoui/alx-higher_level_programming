#include<stdio.h>
#include<stdlib.h>
#include<Python.h>
#include<bytesobject.h>
/*
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: void
*/
void print_python_list(PyObject *p)
{
    int i;
    PyObject *item;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < Py_SIZE(p); i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
/*
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject
 * Return: void
*/
void print_python_bytes(PyObject *p)
{
    int i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    printf("  size: %ld\n", Py_SIZE(p));
    printf("  trying string: %s\n", bytes->ob_sval);
    if (Py_SIZE(p) > 10)
        printf("  first 10 bytes: ");
    else
        printf("  first %ld bytes: ", Py_SIZE(p) + 1);
    for (i = 0; i < Py_SIZE(p) + 1 && i < 10; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i + 1 < Py_SIZE(p) + 1 && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}