#include"funs.h"
#include"notarray.h"
//附加 debug
#include <iostream>
//Vars settings
extern unsigned int SCR_WIDTH;
extern unsigned int SCR_HEIGHT;
//Vars settings
//extern PointData paper;
//extern PointData wall;
int mainxzcvsf()
{
    GLFWwindow* window = GLAWInit();
    {
        if (window == NULL)
        {
            std::cout << "Failed to create GLFW window" << std::endl;
            glfwTerminate();
            return -1;
        }
        glfwMakeContextCurrent(window);
        glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
        // glad: load all OpenGL function pointers
        if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
        {
            std::cout << "Failed to initialize GLAD" << std::endl;
            return -1;
        }
        debugMode();
    }   //Basic
    Shader osha1("shad/vshad2.txt", "shad/fshad2.txt"); 
    unsigned int VBO[2], VAO[2];
    glGenVertexArrays(2, VAO);
    glGenBuffers(2, VBO);

    noar::PointfragData vertex = noar::pointTach(noar::wall_vers, noar::wall_col);
    vertex = noar::pointTach(vertex, noar::wall_texh);
    //DGL_Dataframe2(VAO[0], VBO[0], wall.size, wall.data);
    int _vertex[] = { noar::wall_vers.classnum,
        noar::wall_col.classnum,
        noar::wall_texh.classnum};
    NODGL_Dataframe3(VAO[0], VBO[0], vertex, _vertex);

    unsigned int texture1, texture2, texture3;
    // texture 1
    // ---------
    glGenTextures(1, &texture1);
    glBindTexture(GL_TEXTURE_2D, texture1);
    // set the texture wrapping parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT);	// set texture wrapping to GL_REPEAT (default wrapping method)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    // set texture filtering parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    // load image, create texture and generate mipmaps
    int width, height, nrChannels;

    stbi_set_flip_vertically_on_load(true); // tell stb_image.h to flip loaded texture's on the y-axis.
    // The FileSystem::getPath(...) is part of the GitHub repository so we can find files on any IDE/platform; replace it with your own image path.
    unsigned char* data = stbi_load("PIC/awesomeface.jpg", &width, &height, &nrChannels, 0);
    if (data)
    {
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
        glGenerateMipmap(GL_TEXTURE_2D);
    }
    else
    { 
        std::cout << "Failed to load texture" << std::endl;
    }
    stbi_image_free(data);
    genstexture(texture2, "PIC/wall.jpg");
    genstexture(texture3, "PIC/woodbox.jpg");
    osha1.use();
    //使用.use以后 再使用各种
    osha1.setInt("texture1", 0);
    osha1.setInt("texture2", 1);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, texture1);
    glActiveTexture(GL_TEXTURE1);
    glBindTexture(GL_TEXTURE_2D, texture2);
    //
    // GL_TEXTURE0代表同时能启用的材质 的 最大数
    // Active之后 Bind是替换性的 因此  可以在渲染中途 调整要渲染的图
    // 等所有图转载好 到 所有 图元上即可 绘制（这样解释流畅！）
    //
    while(!glfwWindowShouldClose(window))
    {
        processInput(window);
        
        // or set it 
        //glActiveTexture(GL_TEXTURE1);
        //glBindTexture(GL_TEXTURE_2D, texture3);

        glClearColor(0.2f, 0.3f, 0.6f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        osha1.setBool("tex", true);
        osha1.setFloat("timei", 0.5);

        glBindVertexArray(VAO[0]);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}







// GL_MIRRORED_REPEAT        镜像延申
// GL_REPEAT                 fract延申
// GL_CLAMP_TO_EDGE          甩尾sdf延申
// GL_CLAMP_TO_BORDER        外边全是我们指定的颜色  下面的提前设置好更稳妥
// float borderColor[] = { 1.0f, 1.0f, 0.0f, 1.0f };
// glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, borderColor);
//

//GL_NEAREST    GL_LINEAR
// 光栅时 GL_NEAREST 采用临近法取色 因此常会有像素感
// GL_LINEAR  则对周遭颜色进行采样 因此 会更平滑
// -------------------------------------------------
//多级渐远项
//      GL_NEAREST_MIPMAP_NEAREST	使用最邻近的多级渐远纹理来匹配像素大小，并使用邻近插值进行纹理采样
//      GL_LINEAR_MIPMAP_NEAREST	使用最邻近的多级渐远纹理级别，并使用线性插值进行采样
//      GL_NEAREST_MIPMAP_LINEAR	在两个最匹配像素大小的多级渐远纹理之间进行线性插值，使用邻近插值进行采样
//      GL_LINEAR_MIPMAP_LINEAR	在两个邻近的多级渐远纹理之间使用线性插值，并使用线性插值进行采样
// 
//  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
//  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

//MAG放大时 不应当选择 多级渐远项其一   （GL_INVALID_ENUM错误代码。）