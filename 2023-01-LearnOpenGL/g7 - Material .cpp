
#include"funs.h"
int mainzxvh()
{
    glm::vec3 lights = glm::vec3(1.0, 1.0, 1.0);
    glm::vec3 lightPos(1.2f, 1.0f, 2.0f);

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
    Shader lightingShader("shad2/3materialvs.glsl", "shad2/3materialfs.glsl");
    Shader lightCubeShader("shad2/2lightcubevs.txt", "shad2/2lightcubefs.txt");

    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    noar::PointfragData vertex0 = noar::pointTach(noar::cube_vers, noar::cube_norvec);
    int _vertex0[] = { noar::cube_vers.classnum,noar::cube_vers.classnum };
    NODGL_Dataframe2(VAO, VBO, vertex0, _vertex0);


    unsigned int lightCubeVAO;
    glGenVertexArrays(1, &lightCubeVAO);
    glBindVertexArray(lightCubeVAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    // note that we update the lamp's position attribute's stride to reflect the updated buffer data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    float timeb = glfwGetTime() * float(1.0 * 0.5);
    while (!glfwWindowShouldClose(window))
    {

        float currentFrame = static_cast<float>(glfwGetTime());
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;
        timeb = glfwGetTime() * float(1.0 * 0.2);
        lightPos = glm::vec3(2.0f * sin(timeb), 1.0f, 2.0f * cos(timeb));
        CameraInput(window);
        glClearColor(0.2f, 0.3f, 0.5f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        
        //
        lightingShader.use();
        lightingShader.setVec3("light.position", lightPos);
        lightingShader.setVec3("viewPos", camera.Position);

        // light properties
        glm::vec3 lightColor;
        lightColor.x = static_cast<float>(sin(glfwGetTime() * 2.0));
        lightColor.y = static_cast<float>(sin(glfwGetTime() * 0.7));
        lightColor.z = static_cast<float>(sin(glfwGetTime() * 1.3));
        lightColor = glm::vec3(1.0f,0.95f,0.90f);
        // lightColor为光源的 真实颜色
        // diffuseColor 作为 方向性漫反射 与材质的 漫反射diffuse 和 diff强度（由方向得出）相乘
        // 
        // How to connect
        // 光照的颜色 往往是不动的  物体的颜色作为主导 在三种情况下与 光的颜色相乘
        // A * （b1 +b2 +b3） 环境  方向性直射或慢反射  还有镜面反射
        // 环境光下；直射下和镜面反射下反射什么光
        //
        glm::vec3 diffuseColor = lightColor * glm::vec3(0.8f); // decrease the influence  降低影响
        glm::vec3 ambientColor = diffuseColor * glm::vec3(0.2f); // low influence 

        lightingShader.setVec3("light.ambient", ambientColor);
        lightingShader.setVec3("light.diffuse", diffuseColor);
        lightingShader.setVec3("light.specular", 1.0f, 1.0f, 1.0f);

        // material properties
        lightingShader.setVec3("material.ambient", 0.135f, 0.2225f, 0.1575f);
        lightingShader.setVec3("material.diffuse", 0.54f, 0.89f, 0.63f);
        lightingShader.setVec3("material.specular", 0.316228f, 0.316228f, 0.316228f); // specular lighting doesn't have full effect on this object's material
        lightingShader.setFloat("material.shininess", 0.1f*128.0f);
        /*
        lightingShader.setVec3("material.ambient", 0.0f, 0.1f, 0.06f);
        lightingShader.setVec3("material.diffuse", 0.0f, 0.50980392f, 0.50980392f);
        lightingShader.setVec3("material.specular", 0.50196078f, 0.50196078f, 0.50196078f);
        lightingShader.setFloat("material.shininess", 32.0f);
        */
        // view/projection transformations

        glm::mat4 projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
        glm::mat4 view = camera.GetViewMatrix();
        lightingShader.setMat4("projection", projection);
        lightingShader.setMat4("view", view);

        // world transformation
        glm::mat4 model = glm::mat4(1.0f);
        model = glm::scale(model, glm::vec3(5.0f,1.0f,5.0f));
        lightingShader.setMat4("model", model);

        // render the cube
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 36);

        // also draw the lamp object
        lightCubeShader.use();
        lightCubeShader.setMat4("projection", projection);
        lightCubeShader.setMat4("view", view);
        model = glm::mat4(1.0f);
        model = glm::translate(model, lightPos);
        model = glm::scale(model, glm::vec3(0.2f)); // a smaller cube
        lightCubeShader.setMat4("model", model);
        lightCubeShader.setVec3("realcolor", lightColor);
        glBindVertexArray(lightCubeVAO);
        glDrawArrays(GL_TRIANGLES, 0, 36);

        //
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();

    return 0;
}