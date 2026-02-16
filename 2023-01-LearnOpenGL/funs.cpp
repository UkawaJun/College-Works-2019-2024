#include"funs.h"
#include "notarray.h"
//删掉DEBUG可以关闭调试信息
#define DEBUG
unsigned int SCR_WIDTH = 900;
unsigned int SCR_HEIGHT = 900;

bool firstMouse = true;
float lastX = SCR_WIDTH / 2.0f;
float lastY = SCR_HEIGHT / 2.0f;

float deltaTime = 0.0f;
float lastFrame = 0.0f;
GLFWwindow* GLAWInit()
{
    // glfw: initialize and configure
    // ------------------------------
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    return window;

}
GLFWwindow* GLAWInit(const char * string)
{
    // glfw: initialize and configure
    // ------------------------------
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, string, NULL, NULL);
#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    return window;

}
void debugMode()
{
#ifdef DEBUG
    int nrAttributes;
    glGetIntegerv(GL_MAX_VERTEX_ATTRIBS, &nrAttributes);
    std::cout << "Maximum nr of vertex attributes supported: " << nrAttributes << std::endl;
#endif
}
void genstexture(unsigned int& tar, const char str[])
{
    glGenTextures(1, &tar);
    glBindTexture(GL_TEXTURE_2D, tar);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    int width, height, nrChannels;
    stbi_set_flip_vertically_on_load(true);
    unsigned char* data = stbi_load(str, &width, &height, &nrChannels, 0);
    if (data)
    {//绑定之后，使用之前载入的材质生成纹理 
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
        glGenerateMipmap(GL_TEXTURE_2D);//为当前绑定的纹理自动生成多级渐远纹理
    }
    else std::cout << "Failed to load texture" << std::endl;
    stbi_image_free(data);

}
void processInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
// ---------------------------------------------------------------------------------------------
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}

// layout (location = 1)
void DGL_Dataframe(unsigned int & VAO, unsigned int& VBO,int versize, float *vertices)
{
    glBindVertexArray(VAO);
    //------------follow--------------------------
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, versize, vertices, GL_STATIC_DRAW);
    //------------follow--------------------------
    // position attribute   -- VAO
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // color attribute  --VBO
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);
}
// layout (location = 2)
void DGL_Dataframe2(unsigned int& VAO, unsigned int& VBO, int versize, float* vertices)
{
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, versize, vertices, GL_STATIC_DRAW);
    // position attribute
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // color attribute
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);
    // texture coord attribute
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(6 * sizeof(float)));
    glEnableVertexAttribArray(2);
}
void NODGL_Dataframe3(unsigned int& VAO, unsigned int& VBO, noar::PointfragData vertex,int * _class)
{
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, vertex.truesize, vertex.data, GL_STATIC_DRAW);
    // first attribute
    glVertexAttribPointer(0, *(_class + 0), GL_FLOAT, GL_FALSE, vertex.classnum * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // Second attribute
    glVertexAttribPointer(1, *(_class +1), GL_FLOAT, GL_FALSE, vertex.classnum * sizeof(float), (void*)((*(_class)) * sizeof(float)));
    glEnableVertexAttribArray(1);
    // Third attribute
    glVertexAttribPointer(2, *(_class + 2), GL_FLOAT, GL_FALSE, vertex.classnum * sizeof(float), (void*)((*(_class)+*(_class+1)) * sizeof(float)));
    glEnableVertexAttribArray(2);
}
void NODGL_Dataframe2(unsigned int& VAO, unsigned int& VBO, noar::PointfragData vertex, int *_class)
{
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, vertex.truesize, vertex.data, GL_STATIC_DRAW);
    // first attribute
    glVertexAttribPointer(0, *(_class + 0), GL_FLOAT, GL_FALSE, vertex.classnum * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // Second attribute
    glVertexAttribPointer(1, *(_class + 1), GL_FLOAT, GL_FALSE, vertex.classnum * sizeof(float), (void*)((*(_class)) * sizeof(float)));
    glEnableVertexAttribArray(1);
}
void NODGL_Dataframe1(unsigned int& VAO, unsigned int& VBO, noar::PointfragData vertex, int _class)
{
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, vertex.truesize, vertex.data, GL_STATIC_DRAW);
    // first attribute
    glVertexAttribPointer(0, _class, GL_FLOAT, GL_FALSE, vertex.classnum * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
}
// ------------------------------------------------------------------
//                      camera
// ------------------------------------------------------------------
// glfw: whenever the mouse scroll wheel scrolls, this callback is called
// ----------------------------------------------------------------------
Camera camera(glm::vec3(0.0f, 0.0f, 3.0f));
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset)
{
    camera.ProcessMouseScroll(static_cast<float>(yoffset));
}
void CameraInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);

    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        camera.ProcessKeyboard(FORWARD, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.ProcessKeyboard(BACKWARD, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.ProcessKeyboard(LEFT, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.ProcessKeyboard(RIGHT, deltaTime);
}
// glfw: whenever the window size changed (by OS or user resize) this callback function executes
// ---------------------------------------------------------------------------------------------
// glfw: whenever the mouse moves, this callback is called
// -------------------------------------------------------
void mouse_callback(GLFWwindow* window, double xposIn, double yposIn)
{
    float xpos = static_cast<float>(xposIn);
    float ypos = static_cast<float>(yposIn);

    if (firstMouse)
    {
        lastX = xpos;
        lastY = ypos;
        firstMouse = false;
    }

    float xoffset = xpos - lastX;
    float yoffset = lastY - ypos; // reversed since y-coordinates go from bottom to top

    lastX = xpos;
    lastY = ypos;

    camera.ProcessMouseMovement(xoffset, yoffset);
}


//---------------------------------------------------------------------
// set up vertex data (and buffer(s)) and configure vertex attributes
// 
//      old vertex data in there!
/*
PointData triangle =
{ sizeof(vertice_tai) , sizeof(vertice_tai)/ sizeof(vertice_tai[0]) , vertice_tai,3};
PointData tripaper =
{ sizeof(vertice_taip) , sizeof(vertice_taip) / sizeof(vertice_taip[0]) , vertice_taip,3 };
PointData paper = 
{ sizeof(vertice_block) , sizeof(vertice_block) / sizeof(vertice_block[0]) , vertice_block ,6};
PointData wall=
{ sizeof(vertice_wall) , sizeof(vertice_wall) / sizeof(vertice_wall[0]) , vertice_wall , 6 };
PointData cube =
{ sizeof(vertices_cube) , sizeof(vertices_cube) / sizeof(vertices_cube[0]) , vertices_cube , 36 };
*/