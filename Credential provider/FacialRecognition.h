#ifndef FacialRecognition_H
#define FacialRecognition_H

using namespace std;
#include "CSampleCredential.h"


#include <unknwn.h>
#include "CSampleCredential.h"


#include <windows.h>
#include "bthdef.h"
#include "BluetoothAPIs.h"
#include <tchar.h>
#include <string>
#include <iostream>
#include <vector>
#include <ws2bth.h>

class FacialRecognition
{

public:
	static bool getFace();

};

#endif 
