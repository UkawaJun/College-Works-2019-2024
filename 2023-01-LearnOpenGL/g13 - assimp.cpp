
#include "model.h"
#include "funs.h"

#include <iostream>
int main()
{

	glm::vec3 lights = glm::vec3(1.0, 1.0, 1.0);
	glm::vec3 lightPos(1.2f, 1.0f, 2.0f);
    
    GLFWwindow * window = GLAWInit();
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
    // tell stb_image.h to flip loaded texture's on the y-axis (before loading model).
    stbi_set_flip_vertically_on_load(true);
    glEnable(GL_DEPTH_TEST); 
     
    Model ourModel("model/objs/nanosuit.obj"); 
    Model ourModel2("model/gsofa/sofa.obj");
    Shader ourShader("shad4/1.model_loadingvs.glsl", "shad4/1.model_loadingfs.glsl");
    // draw in wireframe
    //glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     
    // render loop 
    // ----------- 
    glm::vec3 lightColor;  
    float timeb;
    while (!glfwWindowShouldClose(window)) 
    {
        // per-frame time logic 
        // --------------------
        float currentFrame = static_cast<float>(glfwGetTime());
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;

        // input
        // -----
        timeb = glfwGetTime() * float(1.0 * 0.2);
        timeb *= 7.0f;
        CameraInput(window);
        lightPos = glm::vec3(2.0f * sin(timeb), 1.0f, 2.0f * cos(timeb));
        timeb = sin(timeb);
        // render
        // ------
        glClearColor(0.75f, 0.75f, 0.45f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        // don't forget to enable shader before setting uniforms
        ourShader.use(); 
        ourShader.setVec3("light.position", lightPos);
        ourShader.setVec3("viewPos", camera.Position);

        // view/projection transformations 
        glm::mat4 projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
        glm::mat4 view = camera.GetViewMatrix();
        ourShader.setMat4("projection", projection);
        ourShader.setMat4("view", view);
        //ourShader.setVec3("basic_color ", 1.0, 0.0, 0.0);
        //s  
        lightColor = glm::vec3(1.0f, 0.95f, 0.90f);

        glm::vec3 diffuseColor = lightColor * glm::vec3(0.8f); // decrease the influence  ΩµµÕ”∞œÏ
        glm::vec3 ambientColor = diffuseColor * glm::vec3(0.3f); // low influence 

        ourShader.setVec3("light.ambient", ambientColor);
        ourShader.setVec3("light.diffuse", diffuseColor); 
        ourShader.setVec3("light.specular", 1.0f, 1.0f, 1.0f);
          
        // material properties
        ourShader.setVec3("material.ambient", 0.135f, 0.2225f, 0.1575f);
        ourShader.setVec3("material.diffuse", 0.54f, 0.89f, 0.63f);
        ourShader.setVec3("material.specular", 0.316228f, 0.316228f, 0.316228f); // specular lighting doesn't have full effect on this object's material
        ourShader.setFloat("material.shininess", 0.1f * 128.0f);
         
        // render the loaded model 
        glm::mat4 model = glm::mat4(1.0f);
        model = glm::translate(model, glm::vec3(0.0f, 0.0f, 0.0f)); // translate it down so it's at the center of the scene
        model = glm::scale(model, glm::vec3(0.1f, 0.1f, 0.1f));	// it's a bit too big for our scene, so scale it down
        ourShader.setMat4("model", model);
        ourModel.Draw(ourShader);
         
        model = glm::mat4(1.0f); 
        model = glm::translate(model, glm::vec3(5.0f, 0.0f, 0.0f)); // translate it down so it's at the center of the scene
        model = glm::scale(model, glm::vec3(0.1f, 0.1f, 0.1f));	// it's a bit too big for our scene, so scale it down
        ourShader.setMat4("model", model);
        ourModel2.Draw(ourShader);
        
        // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        // -------------------------------------------------------------------------------
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // glfw: terminate, clearing all previously allocated GLFW resources.
    // ------------------------------------------------------------------
    glfwTerminate();
    return 0;
}