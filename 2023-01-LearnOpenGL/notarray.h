#pragma once

#ifndef NOTARRAY_H
#define NOTARRAY_H
#include<iostream>
namespace noar
{
	struct PointfragData
	{
		float* data;	//Array data
		int size;		//Array size
		int classnum;	//Array class size
		int truesize;	//sizeof()
	};
	extern PointfragData cube_vers;
	extern PointfragData cube_col;
	extern PointfragData cube_texh;
	extern PointfragData cube_norvec;

	extern PointfragData wall_vers;
	extern PointfragData wall_col;
	extern PointfragData wall_texh;

	extern PointfragData train_vers;
	extern PointfragData train_col;
	extern PointfragData train_texh;
	//----------------
	//		function
	void printarray(float* array, int size);
	void printarray(const char* name, float* array, int size);
	float* arrayTach(PointfragData a, PointfragData b);
	float* arraysum(float* array1, float* array2, int size1, int size2);

	PointfragData pointTach(PointfragData a, PointfragData b);
	void noarTest();
}
#endif // !NOTARRAY_H


