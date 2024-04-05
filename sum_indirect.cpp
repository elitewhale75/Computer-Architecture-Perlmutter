#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



void setup(int64_t N, uint64_t A[]) {
	printf(" inside sum_indirect problem_setup, N=%lld \n", N);
	for ( int64_t i = 0 ; i < N ; i++ ){
		A[i] = lrand48() % N;
	}
}

int64_t sum(int64_t N, uint64_t A[]) {
	int64_t result, index;

	result = 0;
	index = 0;
	for ( int64_t i = 0 ; i < N ; i++ ){
		result += A[index];
		index = A[index];
	}

	printf(" inside sum_indirect perform_sum, N=%lld \n", N);

	return result;
}

