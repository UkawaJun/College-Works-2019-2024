#ifndef MAS_H
#define MAS_H
#include"shader.h"
namespace shamas
{
	//lights
	void setLight_dark(Shader tar, glm::vec3 lightColor);
	void setLight_verydark(Shader tar, glm::vec3 lightColor);
	void setLight_light(Shader tar, glm::vec3 lightColor);
	void setLight_verylight(Shader tar, glm::vec3 lightColor);
	//ÓñÊ¯
	void setMaterial_jade(Shader tar);
	//ÂÌ±¦Ê¯
	void setMaterial_emerald(Shader tar);
	//ºÚê×Ê¯
	void setMaterial_obsidian(Shader tar);
	//ÕäÖé
	void setMaterial_pearl(Shader tar);
	//ºì±¦Ê¯
	void setMaterial_ruby(Shader tar);
	//ÂÌËÉÊ¯
	void setMaterial_turquoise(Shader tar);

	//»ÆÍ­
	void setMaterial_brass(Shader tar);
	//ÇàÍ­
	void setMaterial_bronze(Shader tar);
	//¸õ
	void setMaterial_chrome(Shader tar);
	//Í­
	void setMaterial_copper(Shader tar);
	//½ğ
	void setMaterial_gold(Shader tar);
	void setMaterial_PolishedGold(Shader tar);
	//Òø
	void setMaterial_silver(Shader tar);
	void setMaterial_PolishedSilver(Shader tar);
	//Îı
	void setMaterial_tin(Shader tar);

	//ºÚÉ«Ïğ½º
	void setMaterial_blackRubber(Shader tar);
	//ÇàÉ«Ïğ½º
	void setMaterial_cyanRubber(Shader tar);
	//ÂÌÉ«Ïğ½º
	void setMaterial_greenRubber(Shader tar);
	//ºìÉ«Ïğ½º
	void setMaterial_redRubber(Shader tar);
	//°×É«Ïğ½º
	void setMaterial_whiteRubber(Shader tar);
	//»ÆÉ«Ïğ½º
	void setMaterial_yellowRubber(Shader tar);
}



#endif