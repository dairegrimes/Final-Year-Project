#include "Clock.h"

void Clock::StartClock()
{
	clock_t start;
	start = clock();
}


double Clock::getClock(clock_t start)
{
	double duration;
	duration = (std::clock() - start) / (double)CLOCKS_PER_SEC;
	return duration;
}