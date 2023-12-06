#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    char *str;
    int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %d\n", size);
    printf("  trying str: %s\n", str);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %d bytes:", limit);

    for (i = 0; i < limit; i++)
        if (str[i] >= 0)
            printf(" %02x", str[i]);
        else
            printf(" %02x", 256 + str[i]);

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = ((PyListObject *)p)->ob_item[i];
        printf("Element %d: %s\n", i, ((obj)->ob_type)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}