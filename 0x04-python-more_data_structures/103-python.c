#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *obj;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);
    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
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