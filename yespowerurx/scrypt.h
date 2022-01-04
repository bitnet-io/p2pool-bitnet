#ifndef SCRYPT_H
#define SCRYPT_H

//#include "yespower/yespower.h"

#ifdef __cplusplus
extern "C" {
#endif

void yespower_tls(const char* input, char* output);
//void _sp(const char* input, char* output, char* scratchpad);
const int scrypt_scratchpad_size = 131583;

#ifdef __cplusplus
}
#endif

#endif
