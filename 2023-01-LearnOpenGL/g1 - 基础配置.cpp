
//gl1
// 基础结构 有封装好的shader使用
// 材质代码的包装（在g1中不适用材质）
// 点集的包装  还有根据设定采用 相关挖点技术的包装-----？ 包装成函数！
//      为什么要做封装     当然是为了方便教学
//      DGL是为了取点才封起来的
//      特别是opengl废话很多时，封装起来相当有奇效！
//      其中最重要的 要解决 一堆c文件放在一起的各种繁复定义的问题
//gl1
//  ---------------------------------------------------  //
// 因此在讲每一个具体的章节时 需要的代码也会被封装成函数 在下一章节使用
// 因此往往 在具体的章节中  不直接使用封装代码  而在下一章使用
// 
// 
// 
//基础 优先
//自声明
#include"funs.h"
#include"notarray.h"
//附加 debug
#include <iostream>
//Vars settings
extern unsigned int SCR_WIDTH;
extern unsigned int SCR_HEIGHT;
//Vars settings

int c = 0;
//extern PointData triangle;
//extern PointData paper;

int mainvb()
{ 
    //--------------这一套可以直接复制的
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
    }
    // build and compile our shader program
    // ------------------------------------
    Shader ourShader("shad/vshad1.txt", "shad/fshad1.txt"); 
    //
    noar::PointfragData vertex = noar::pointTach(noar::train_vers, noar::train_col);
    noar::PointfragData vertex2 = noar::pointTach(noar::wall_vers, noar::wall_col);
    unsigned int VBO[2], VAO[2];
    // glGenVertexArrays(1, &VAO);
    // glGenBuffers(1, &VBO);
    glGenVertexArrays(2, VAO);
    glGenBuffers(2, VBO);
    // bind the Vertex Array Object first, then bind and set vertex buffer(s), and then configure vertex attributes(s).
    glBindVertexArray(VAO[0]);
    //------------follow--------------------------

    glBindBuffer(GL_ARRAY_BUFFER, VBO[0]);
    glBufferData(GL_ARRAY_BUFFER, vertex.truesize, vertex.data, GL_STATIC_DRAW);
    //------------follow--------------------------
    
    // position attribute   -- VAO
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // color attribute  --VBO
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1); 


    //---------------------------------------------------------
    glBindVertexArray(VAO[1]);
    //------------follow--------------------------
    glBindBuffer(GL_ARRAY_BUFFER, VBO[1]);
    glBufferData(GL_ARRAY_BUFFER, vertex2.truesize, vertex2.data, GL_STATIC_DRAW);
    //------------follow--------------------------

    // position attribute   -- VAO
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // color attribute  --VBO
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);


    
    // You can unbind the VAO afterwards so other VAO calls won't accidentally modify this VAO, but this rarely happens. Modifying other
    // VAOs requires a call to glBindVertexArray anyways so we generally don't unbind VAOs (nor VBOs) when it's not directly necessary.
    // glBindVertexArray(0);
    // render loop
    // -----------
    //init
    //glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    //
    float timeb = glfwGetTime() * float(1.0 * 0.5);
    
    while (!glfwWindowShouldClose(window))
    {

        timeb = glfwGetTime() * float(1.0 * 0.6);
        timeb = abs(sin(timeb) + 1.0);

        processInput(window);
        // render 
        glClearColor(0.6f* timeb, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT); 
        
        // render the triangle
        ourShader.use();
        ourShader.setFloat("timei", timeb);
        glBindVertexArray(VAO[1]);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        ourShader.setFloat("timei", timeb*1.0);
        glBindVertexArray(VAO[0]);
        glDrawArrays(GL_TRIANGLES, 0,3);
        // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        // -------------------------------------------------------------------------------
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    /*   最简的版本
    while(!glfwWindowShouldClose(window))
    {
        processInput(window);

        glClearColor(0.6f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
    */

    // optional: de-allocate all resources once they've outlived their purpose:
    // ------------------------------------------------------------------------
    glDeleteVertexArrays(2, VAO);
    glDeleteBuffers(2, VBO);
    // glfw: terminate, clearing all previously allocated GLFW resources.
    // ------------------------------------------------------------------
    glfwTerminate();
    return 0;
}
// ---------------------------------------------------------------------------------------------------------
