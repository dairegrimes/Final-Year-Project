#ifndef PhoneConnected_H
#define PhoneConnected_H

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

class PhoneConnected
{

public:
	static bool scanPhone();

};

#endif 
