
#include "KeystrokeDynamics.h";


KeystrokeDynamics::KeystrokeDynamics()
{

}


KeystrokeDynamics::~KeystrokeDynamics()
{

}







double findDifference(double num1, double num2)
{
	if (num1 == num2)
	{
		return 0;
	}

	else if (num1 > num2)
	{
		return ((num2 / num1) * 100);
	}

	else
	{
		return ((num1 / num2) * 100);
	}
}





void KeystrokeDynamics::getKeystrokes(double duration)
{
	KeySwitchTime.push_back(duration);
}




bool KeystrokeDynamics::getAverage(vector<double> KeySwitchTime)
{
	double storedST[] = { 0.078, 0.072, 0.116, 0.178, 0.165, 0.191, 0.216, 0.043, 0.166, 0.163 };
	

	for (int i = 0; i < KeySwitchTime.size() - 1; i++)
	{
		diff.push_back(KeySwitchTime[i + 1] - KeySwitchTime[i]);
	}


	for (int i = 0; i < KeySwitchTime.size() - 1; i++)
	{
		average.push_back(findDifference(diff[i], storedST[i]));
	}

	for (int i = 0; i < KeySwitchTime.size() - 1; i++)
	{
		total += average[i];
	}

	result = (total / average.size());

	


	if (result >= 70)
	{
		return true;
	}
	else
	{
		return false;
	}
	
	
	ofstream myfile;
	myfile.open("C:\\Users\\daire\\Desktop\\QRCODEFILE.txt");

	for (int i = 0; i < KeySwitchTime.size(); i++)
	{
		myfile << HoldTime[i] << endl;
	}

	myfile.close();
	
	
	



}


