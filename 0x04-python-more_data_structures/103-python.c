#include <stdio.h>
#include <Python.h>
#include <stdlib.h>
/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
/**
 * print_python_bytes - prints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = ((PyVarObject *)p)->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);
    if (size < 10)
        printf("  first %ld bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", string[i]);
    printf("\n");
}
