#include <Python.h>

#include "scrypt.h"

static PyObject *yes_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyStringObject *input;
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);



    yespower_tls((char *)PyString_AsString((PyObject*) input), output);




    Py_DECREF(input);
    value = Py_BuildValue("s#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef ScryptMethods[] = {
    { "getPoWHash", yes_getpowhash, METH_VARARGS, "Returns the proof of work hash using yespowerurx" },

    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC inityes_power(void) {
    (void) Py_InitModule("yespowerurx", ScryptMethods);
}
