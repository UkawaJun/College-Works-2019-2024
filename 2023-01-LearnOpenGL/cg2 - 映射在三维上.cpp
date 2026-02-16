#include "funs.h"
int mainjffg()
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
    Shader ourShader("shad3/2gvs.txt", "shad3/2gfs.txt");
    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    NODGL_Dataframe1(VAO, VBO, noar::cube_vers, noar::cube_vers.classnum);
    glm::mat4 projection = glm::mat4(1.0f);
    glm::mat4 view = glm::mat4(1.0f);

    glm::mat4 models = glm::mat4(1.0f);
    models = glm::rotate(models, glm::radians(90.0f), glm::vec3(0.0, 0.0, 1.0));




    float timeb = glfwGetTime() * float(1.0 * 0.5);
    while (!glfwWindowShouldClose(window))
    {
        float currentFrame = static_cast<float>(glfwGetTime());
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;
        CameraInput(window); 
        timeb = glfwGetTime() * float(1.0 * 0.5);  

        processInput(window);
        models = glm::mat4(1.0f); 
        models = glm::rotate(models, glm::radians(timeb * 20.0f), glm::vec3(0.0, 0.0, 1.0));
        timeb = sin(timeb);
        models = glm::scale(models, glm::vec3(2.0 , 2.0 , 2.0));
         
        projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
        view = camera.GetViewMatrix();
        ourShader.use();
        ourShader.setMat4("model", models);
        ourShader.setMat4("projection", projection); 
        ourShader.setMat4("view", view);
        ourShader.setFloat("timeb",timeb);
        glClearColor(0.8f, 0.3f, 0.3f, 1.0f); 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, noar::cube_vers.size/ noar::cube_vers.classnum);
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}