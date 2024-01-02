#include "Python.h"

/**
 * print_python_string - function that prints infos
 * about a python string object.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int size;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	size = ((PyASCIIObject *)(p))->size;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  size: %ld\n", size);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &size));
}