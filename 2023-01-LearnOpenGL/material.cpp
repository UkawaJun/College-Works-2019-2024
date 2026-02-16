#include"material.h"
// specular lighting doesn't have full effect on this object's material

//shader Note!!!!ÒªÇó£º
/*
struct Material {
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};

struct Light {
    vec3 position;

    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};
*/
void shamas::setLight_dark(Shader tar,glm::vec3 lightColor)
{
    glm::vec3 diffuseColor = lightColor * glm::vec3(0.5f); 
    glm::vec3 ambientColor = diffuseColor * glm::vec3(0.2f); 
    tar.setVec3("light.ambient", ambientColor);
    tar.setVec3("light.diffuse", diffuseColor);
    tar.setVec3("light.specular", 1.0f, 1.0f, 1.0f);
}
void shamas::setLight_verydark(Shader tar, glm::vec3 lightColor)
{
    glm::vec3 diffuseColor = lightColor * glm::vec3(0.3f);
    glm::vec3 ambientColor = diffuseColor * glm::vec3(0.1f);
    tar.setVec3("light.ambient", ambientColor);
    tar.setVec3("light.diffuse", diffuseColor);
    tar.setVec3("light.specular", 1.0f, 1.0f, 1.0f);
}
void shamas::setLight_light(Shader tar, glm::vec3 lightColor)
{
    glm::vec3 diffuseColor = lightColor * glm::vec3(0.8f);
    glm::vec3 ambientColor = diffuseColor * glm::vec3(0.5f);
    tar.setVec3("light.ambient", ambientColor);
    tar.setVec3("light.diffuse", diffuseColor);
    tar.setVec3("light.specular", 1.0f, 1.0f, 1.0f);
}
void shamas::setLight_verylight(Shader tar, glm::vec3 lightColor)
{
    glm::vec3 diffuseColor = lightColor;
    glm::vec3 ambientColor = diffuseColor* glm::vec3(0.7f);
    tar.setVec3("light.ambient", ambientColor);
    tar.setVec3("light.diffuse", diffuseColor);
    tar.setVec3("light.specular", 1.0f, 1.0f, 1.0f);
}
void shamas::setMaterial_jade(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.135,0.2225,0.1575);
    tar.setVec3("material.diffuse", 0.54,0.89,0.63);
    tar.setVec3("material.specular", 0.316228,0.316228,0.316228);
    float shininess = 0.1f      ;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ÂÌ±¦Ê¯
void shamas::setMaterial_emerald(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.0215	,0.1745	,0.0215);
    tar.setVec3("material.diffuse", 0.07568	,0.61424	,0.07568);
    tar.setVec3("material.specular", 0.633	,0.727811	,0.633);
    float shininess = 0.6f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ºÚê×Ê¯
void shamas::setMaterial_obsidian(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.05375	,0.05	,0.06625);
    tar.setVec3("material.diffuse", 0.18275	,0.17	,0.22525);
    tar.setVec3("material.specular", 0.332741	,0.328634	,0.346435);
    float shininess = 0.3f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ÕäÖé
void shamas::setMaterial_pearl(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.25	,0.20725	,0.20725);
    tar.setVec3("material.diffuse", 1	,0.829	,0.829);
    tar.setVec3("material.specular", 0.296648	,0.296648	,0.296648);
    float shininess = 0.088f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ºì±¦Ê¯
void shamas::setMaterial_ruby(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.1745	,0.01175	,0.01175);
    tar.setVec3("material.diffuse", 0.61424	,0.04136	,0.04136);
    tar.setVec3("material.specular", 0.727811	,0.626959	,0.626959);
    float shininess = 0.6f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ÂÌËÉÊ¯
void shamas::setMaterial_turquoise(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.1	,0.18725	,0.1745);
    tar.setVec3("material.diffuse", 0.396	,0.74151	,0.69102);
    tar.setVec3("material.specular", 0.297254	,0.30829	,0.306678);
    float shininess = 0.1f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//»ÆÍ­
void shamas::setMaterial_brass(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.329412	,0.223529	,0.027451);
    tar.setVec3("material.diffuse", 0.780392	,0.568627	,0.113725);
    tar.setVec3("material.specular", 0.992157	,0.941176	,0.807843);
    float shininess = 0.21794872f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ÇàÍ­
void shamas::setMaterial_bronze(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.2125	,0.1275	,0.054);
    tar.setVec3("material.diffuse", 0.714	,0.4284	,0.18144);
    tar.setVec3("material.specular", 0.393548	,0.271906	,0.166721);
    float shininess = 0.2f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//¸õ
void shamas::setMaterial_chrome(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.25	,0.25	,0.25);
    tar.setVec3("material.diffuse", 0.4	,0.4	,0.4);
    tar.setVec3("material.specular", 0.774597	,0.774597	,0.774597);
    float shininess = 0.6f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//Í­
void shamas::setMaterial_copper(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.19125	,0.0735	,0.0225);
    tar.setVec3("material.diffuse", 0.7038	,0.27048,	0.0828);
    tar.setVec3("material.specular", 0.256777	,0.137622	,0.086014);
    float shininess = 0.1f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//½ð
void shamas::setMaterial_gold(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.24725	,0.1995	,0.0745);
    tar.setVec3("material.diffuse", 0.75164	,0.60648	,0.22648);
    tar.setVec3("material.specular", 0.628281	,0.555802	,0.366065);
    float shininess = 0.4f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
void shamas::setMaterial_PolishedGold(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.24725f, 0.2245f, 0.0645f);
    tar.setVec3("material.diffuse", 0.34615f, 0.3143f, 0.0903f);
    tar.setVec3("material.specular", 0.797357f, 0.723991f, 0.208006f);
    tar.setFloat("material.shininess", 83.2f);
}
//ÂÌËÉÊ¯
void shamas::setMaterial_tin(Shader tar)
{
    tar.setVec3("material.ambient", 0.105882f, 0.058824f, 0.113725f);
    tar.setVec3("material.diffuse", 0.427451f, 0.470588f, 0.541176f);
    tar.setVec3("material.specular", 0.333333f, 0.333333f, 0.521569f);
    tar.setFloat("material.shininess", 9.84615f);
}
//Òø
void shamas::setMaterial_silver(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.19225	,0.19225	,0.19225);
    tar.setVec3("material.diffuse", 0.50754	,0.50754	,0.50754);
    tar.setVec3("material.specular", 0.508273	,0.508273	,0.508273);
    float shininess = 0.4f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
void shamas::setMaterial_PolishedSilver(Shader tar)
{
    tar.setVec3("material.ambient", 0.23125f, 0.23125f, 0.23125f);
    tar.setVec3("material.diffuse", 0.2775f, 0.2775f, 0.2775f);
    tar.setVec3("material.specular", 0.773911f, 0.773911f, 0.773911f);
    tar.setFloat("material.shininess", 89.6f);
}

//ºÚÉ«Ïð½º
void shamas::setMaterial_blackRubber(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.02	,0.02	,0.02);
    tar.setVec3("material.diffuse", 0.01	,0.01	,0.01);
    tar.setVec3("material.specular", 0.4	,0.4	,0.4);
    float shininess = 0.078125f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ÇàÉ«Ïð½º
void shamas::setMaterial_cyanRubber(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.0	,0.05	,0.05);
    tar.setVec3("material.diffuse", 0.4	,0.5	,0.5);
    tar.setVec3("material.specular", 0.04	,0.7	,0.7);
    float shininess = 0.078125f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ÂÌÉ«Ïð½º
void shamas::setMaterial_greenRubber(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.0	,0.05	,0.0);
    tar.setVec3("material.diffuse", 0.4	,0.5	,0.4);
    tar.setVec3("material.specular", 0.04	,0.7	,0.04);
    float shininess = 0.078125f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//ºìÉ«Ïð½º
void shamas::setMaterial_redRubber(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.05	,0.0	,0.0);
    tar.setVec3("material.diffuse", 0.5	,0.4	,0.4);
    tar.setVec3("material.specular", 0.7	,0.04	,0.04);
    float shininess = 0.078125f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//°×É«Ïð½º
void shamas::setMaterial_whiteRubber(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.05	,0.05	,0.05);
    tar.setVec3("material.diffuse", 0.5	,0.5	,0.5);
    tar.setVec3("material.specular", 0.7	,0.7	,0.7);
    float shininess = 0.078125f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}
//»ÆÉ«Ïð½º
void shamas::setMaterial_yellowRubber(Shader tar)
{
    // material properties
    tar.setVec3("material.ambient", 0.05	,0.05	,0.0);
    tar.setVec3("material.diffuse", 0.5	,0.5	,0.4);
    tar.setVec3("material.specular", 0.7	,0.7	,0.04);
    float shininess = 0.078125f;
    tar.setFloat("material.shininess", shininess * 128.0f);
}