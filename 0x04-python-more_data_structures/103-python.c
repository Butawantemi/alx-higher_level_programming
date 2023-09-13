#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
* Print_python_list - print information about a Python list
* @p: A Python object (Assumed to be a list)
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;
size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
* Print_python_bytes - print information about a Python bytes object
* @p: A Python object (assumed to be bytes)
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *data;
printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
data = PyBytes_AsString(p);
printf("  size: %zd\n", size);
printf("  trying string: %s\n", data);
printf("  first %zd bytes:", size + 1 < 10 ? size + 1 : 10);
for (i = 0; i < size + 1 && i < 10; i++)
printf(" %02x", data[i] & 0xff);
printf("\n");
}
