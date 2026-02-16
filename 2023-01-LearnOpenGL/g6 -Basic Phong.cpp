//
//      环境光照(Ambient Lighting)：
// 即使在黑暗的情况下，世界上通常也仍然有一些光亮（月亮、远处的光），
// 所以物体几乎永远不会是完全黑暗的。为了模拟这个，我们会使用一个环境光照常量，它永远会给物体一些颜色。
// 
//      漫反射光照(Diffuse Lighting)：
// 模拟光源对物体的方向性影响(Directional Impact)。它是冯氏光照模型中视觉上最显著的分量。
// 物体的某一部分越是正对着光源，它就会越亮。
// 
//      镜面光照(Specular Lighting)：
// 模拟有光泽物体上面出现的亮点。
// 镜面光照的颜色相比于物体的颜色会更倾向于光的颜色。
// 



#include"funs.h"
glm::vec3 lights = glm::vec3(1.0, 1.0, 1.0);
glm::vec3 lightPos(1.2f, 1.0f, 2.0f);
int mainzxc()
{
    //完全基础的 摄像机系统 直接复制
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
        glfwSetCursorPosCallback(window, mouse_callback);
        glfwSetScrollCallback(window, scroll_callback);
        // tell GLFW to capture our mouse
        glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
        // glad: load all OpenGL function pointers
        if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
        {
            std::cout << "Failed to initialize GLAD" << std::endl;
            return -1;
        }
        debugMode();
    }
    glEnable(GL_DEPTH_TEST);
    //Complete Camera system!
    Shader lightingShader("shad2/2colorsvs.txt", "shad2/2colorsfs.txt");
    Shader lightCubeShader("shad2/2lightcubevs.txt", "shad2/2lightcubefs.txt");
    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO); 
    glGenBuffers(1, &VBO);
    //          ---------------------
    // be sure to activate shader when setting uniforms/drawing objects 
    glm::mat4 projection = glm::mat4(1.0f);
    glm::mat4 view = glm::mat4(1.0f);
    glm::mat4 model = glm::mat4(1.0f);
    
    noar::PointfragData vertex0 = noar::pointTach(noar::cube_vers, noar::cube_norvec);
    int _vertex0[] = { noar::cube_vers.classnum,noar::cube_vers.classnum };
    NODGL_Dataframe2(VAO, VBO, vertex0, _vertex0);
    //std::cout << vertex0.classnum;
    

    float timeb = glfwGetTime() * float(1.0 * 0.5);
    while (!glfwWindowShouldClose(window))
    { 
        
        float currentFrame = static_cast<float>(glfwGetTime());
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;
        timeb = glfwGetTime() * float(1.0 * 0.2);
          
        lightPos = glm::vec3(2.0f * sin(timeb),1.0f, 2.0f * cos(timeb));
        timeb = sin(timeb);
        
        timeb *= timeb; 
        glClearColor(0.2f, 0.3f, 0.5f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        CameraInput(window);

        lightingShader.use();
        lightingShader.setVec3("objectColor", 1.0f, 0.5f, 0.31f);
        lightingShader.setVec3("lightColor", lights);
        lightingShader.setVec3("lightPos", lightPos);
        lightingShader.setVec3("viewPos", camera.Position);
        // view/projection transformations
        projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
        view = camera.GetViewMatrix();
        lightingShader.setMat4("projection", projection);
        lightingShader.setMat4("view", view);

        // world transformation
        model = glm::mat4(1.0f);
        model = glm::scale(model, glm::vec3(5.0, 1.0, 5.0));
        lightingShader.setMat4("model", model);
        lightingShader.setFloat("ambientStrength",0.3);
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 36);

        lightCubeShader.use();
        lightCubeShader.setMat4("projection", projection);
        lightCubeShader.setMat4("view", view);
        lightCubeShader.setVec3("realcolor", lights);
        model = glm::mat4(1.0f);
        model = glm::translate(model, lightPos);
        model = glm::scale(model, glm::vec3(0.2f)); // a smaller cube
        lightCubeShader.setMat4("model", model);

        glDrawArrays(GL_TRIANGLES, 0, 36);
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();

	return 0;
}