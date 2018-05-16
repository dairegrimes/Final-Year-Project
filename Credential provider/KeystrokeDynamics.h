#ifndef KeystrokeDynamics_H
#define KeystrokeDynamics_H

using namespace std;


#include <windows.h>
#include "bthdef.h"
#include <tchar.h>
#include <string>
#include <iostream>
#include <vector>
#include <ws2bth.h>
#include <ctime>
#include <cstdio>
#include <vector>
#include <conio.h>
#include <ciso646>
#include "Clock.h"
#include <fstream>
#include <thread>

class KeystrokeDynamics
{

public:

	KeystrokeDynamics();
	~KeystrokeDynamics();
	
	vector<double> KeySwitchTime;
	vector <double> HoldTime;

	vector<double> diff;
	vector<double> average;
	void getKeystrokes(double duration);
	void getHoldTime(double duration);
	
	void startKeystroke();
	

	double total = 0;
	double result = 0;
	
	double readkey(double duration);

	bool getAverage(vector<double> KeySwitchTime);

	



private:

	

};

#endif 

// C:\\Users\\daire\\Desktop\\QRCODEFILE.txt
