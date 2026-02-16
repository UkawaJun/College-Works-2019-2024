#pragma once
#ifndef FUNS_C


#define FUNS_C
#include <openGL/glad.h>

#include <GLFW/glfw3.h>
#include"stb_image.h"
#include "shader.h"
#include<math.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include"camera.h"
#include"notarray.h"

#include<iostream>
//extern float vertice_tai[];
//extern int  vertice_tai_size;
void genstexture(unsigned int& tar, const char str[]);
void processInput(GLFWwindow* window);
void framebuffer_size_callback(GLFWwindow* window, int width, int height);
GLFWwindow* GLAWInit();
GLFWwindow* GLAWInit(const char* string);
void debugMode();
//两个旧的取点函数
void DGL_Dataframe(unsigned int& VAO, unsigned int& VBO, int versize, float* vertices);
void DGL_Dataframe2(unsigned int& VAO, unsigned int& VBO, int versize, float* vertices);
//-----------------------------------------------------
struct PointData
{
	int size;
	int pointsize;
	float *data;
	int pointNum;		//drawArray
};
/*		finitued in 2022 12 29
extern PointData triangle;		//no texture
extern PointData tripaper;		// textured
extern PointData paper;			//no texture
extern PointData wall;			// textured

extern PointData cube;			//texture
extern PointData block;			//no texture

*/
//--------------
//	camera
//--------------
extern Camera camera;
extern bool firstMouse;
extern unsigned int SCR_WIDTH;
extern unsigned int SCR_HEIGHT;
extern float  lastX;
extern float  lastY;
extern float deltaTime;
extern float lastFrame;
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);
void mouse_callback(GLFWwindow* window, double xpos, double ypos);
void CameraInput(GLFWwindow* window);

//not array
void NODGL_Dataframe3(unsigned int& VAO, unsigned int& VBO, noar::PointfragData vertex, int* _class);
void NODGL_Dataframe2(unsigned int& VAO, unsigned int& VBO, noar::PointfragData vertex, int* _class);
void NODGL_Dataframe1(unsigned int& VAO, unsigned int& VBO, noar::PointfragData vertex, int  _class);
//
#endif