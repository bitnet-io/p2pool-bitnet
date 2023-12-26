#include <Python.h>

//#include "scrypt.h"
#include "aurum.h"

static PyObject *scrypt_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyStringObject *input;
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

// THIS DOESNT WORK HERE FOR AURUM    
//scrypt_1024_1_1_256((char *)PyString_AsString((PyObject*) input), output);


aurum_hash((char *)PyString_AsString((PyObject*) input), output);
    Py_DECREF(input);
    value = Py_BuildValue("s#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef ScryptMethods[] = {
    { "getPoWHash", scrypt_getpowhash, METH_VARARGS, "Returns the proof of work hash using aurum" },
    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initaurum_hash(void) {
    (void) Py_InitModule("aurum_hash", ScryptMethods);
}
