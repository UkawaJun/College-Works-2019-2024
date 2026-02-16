#include"notarray.h"
using namespace noar;

float* noar::arraysum(float* array1, float* array2, int size1, int size2)
{   //use for GL        合并两个数组 返回其地址
    float* iss = new float[size1 + size2]{ 0.0 };
    int ful = size1 + size2;
    for (int i = 0; i < size1; i++) *(iss + i) = *(array1 + i);
    for (int i = 0; i < size2; i++) *(iss + i + size1) = *(array2 + i);
    return iss;
}
PointfragData noar::pointTach(PointfragData a, PointfragData b)
{
    bool is_a = true;
    int fov = 0;
    int sum_size = a.size + b.size;

    int inita = 0, initb = 0;
    float* finals = new float[sum_size] {0.0};
    for (int i = 0; i < sum_size; i++)
    {
        int pov;
        if (is_a) pov = a.classnum;
        else pov = b.classnum;
        //--------------------
        if (is_a) { *(finals + i) = *(a.data + inita); inita++; }
        else { *(finals + i) = *(b.data + initb); initb++; }
        fov++;
        if (fov == pov) { is_a = !is_a; fov = 0; }
    }
    PointfragData retu = { finals,a.size + b.size,a.classnum + b.classnum ,a.truesize+b.truesize};
    return retu;
}
float* noar::arrayTach(PointfragData a, PointfragData b)
{
    bool is_a = true;
    int fov = 0;
    int sum_size = a.size + b.size;

    int inita = 0, initb = 0;
    float* finals = new float[sum_size] {0.0};
    for (int i = 0; i < sum_size; i++)
    {
        int pov;
        if (is_a) pov = a.classnum;
        else pov = b.classnum;
        //--------------------
        if (is_a) { *(finals + i) = *(a.data + inita); inita++; }
        else { *(finals + i) = *(b.data + initb); initb++; }
        fov++;
        if (fov == pov) { is_a = !is_a; fov = 0; }
    }
    return finals;
}

void noar::printarray(float* array, int size)
{
    for (int i = 0; i < size; i++)  std::cout << *(array + i) << "\t";
    std::cout << std::endl << "address:" << array << std::endl;
    std::cout << "size:" << size << std::endl << std::endl;
}

void noar::printarray(const char* name, float* array, int size)
{
    for (int i = 0; i < size; i++)  std::cout << *(array + i) << "\t";
    std::cout << std::endl << "address:" << array << std::endl;
    std::cout << "size:" << size << std::endl;
    std::cout << "name:" << name << std::endl << std::endl;
}
float cube_1[] = {
       -0.5f, -0.5f, -0.5f,
        0.5f, -0.5f, -0.5f,
        0.5f,  0.5f, -0.5f,
        0.5f,  0.5f, -0.5f,
       -0.5f,  0.5f, -0.5f,
       -0.5f, -0.5f, -0.5f,

       -0.5f, -0.5f,  0.5f,
        0.5f, -0.5f,  0.5f,
        0.5f,  0.5f,  0.5f,
        0.5f,  0.5f,  0.5f,
       -0.5f,  0.5f,  0.5f,
       -0.5f, -0.5f,  0.5f,

       -0.5f,  0.5f,  0.5f,
       -0.5f,  0.5f, -0.5f,
       -0.5f, -0.5f, -0.5f,
       -0.5f, -0.5f, -0.5f,
       -0.5f, -0.5f,  0.5f,
       -0.5f,  0.5f,  0.5f,

        0.5f,  0.5f,  0.5f,
        0.5f,  0.5f, -0.5f,
        0.5f, -0.5f, -0.5f,
        0.5f, -0.5f, -0.5f,
        0.5f, -0.5f,  0.5f,
        0.5f,  0.5f,  0.5f,

       -0.5f, -0.5f, -0.5f,
        0.5f, -0.5f, -0.5f,
        0.5f, -0.5f,  0.5f,
        0.5f, -0.5f,  0.5f,
       -0.5f, -0.5f,  0.5f,
       -0.5f, -0.5f, -0.5f,

       -0.5f,  0.5f, -0.5f,
        0.5f,  0.5f, -0.5f,
        0.5f,  0.5f,  0.5f,
        0.5f,  0.5f,  0.5f,
       -0.5f,  0.5f,  0.5f,
       -0.5f,  0.5f, -0.5f
};
float cube_2[] = {
    0.0f, 0.0f, 1.0f,
    1.0f, 0.0f, 1.0f,
    0.0f, 1.0f, 1.0f,
    1.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,

    1.0f, 0.0f, 1.0f,
    0.0f, 1.0f, 1.0f,
    0.0f, 0.0f, 1.0f,
    1.0f, 1.0f, 0.0f,
    1.0f, 0.0f, 0.0f,
    0.0f, 0.0f, 1.0f,

    1.0f, 0.0f, 1.0f,
    1.0f, 1.0f, 0.0f,
    0.0f, 0.0f, 1.0f,
    1.0f, 1.0f, 0.0f,
    1.0f, 0.0f, 0.0f,
    0.0f, 0.0f, 1.0f,

    0.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,
    1.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,

    1.0f, 0.0f, 1.0f,
    0.0f, 1.0f, 1.0f,
    1.0f, 1.0f, 0.0f,
    1.0f, 1.0f, 0.0f,
    1.0f, 0.0f, 0.0f,
    0.0f, 0.0f, 1.0f,

    0.0f, 0.0f, 1.0f,
    1.0f, 0.0f, 1.0f,
    1.0f, 1.0f, 0.0f,
    1.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f,
    0.0f, 0.0f, 1.0f
};
float cube_3[] = {
      0.0f, 0.0f,
      1.0f, 0.0f,
      1.0f, 1.0f,
      1.0f, 1.0f,
      0.0f, 1.0f,
      0.0f, 0.0f,

      0.0f, 0.0f,
      1.0f, 0.0f,
      1.0f, 1.0f,
      1.0f, 1.0f,
      0.0f, 1.0f,
      0.0f, 0.0f,

      1.0f, 0.0f,
      1.0f, 1.0f,
      0.0f, 1.0f,
      0.0f, 1.0f,
       0.0f, 0.0f,
      1.0f, 0.0f,

      1.0f, 0.0f,
      1.0f, 1.0f,
      0.0f, 1.0f,
       0.0f, 1.0f,
      0.0f, 0.0f,
      1.0f, 0.0f,

     0.0f, 1.0f,
      1.0f, 1.0f,
      1.0f, 0.0f,
      1.0f, 0.0f,
      0.0f, 0.0f,
      0.0f, 1.0f,

      0.0f, 1.0f,
       1.0f, 1.0f,
      1.0f, 0.0f,
       1.0f, 0.0f,
      0.0f, 0.0f,
      0.0f, 1.0f
};
float cube_4[] = {
    //normal Vector
    0.0f,  0.0f, -1.0f,
    0.0f,  0.0f, -1.0f,
    0.0f,  0.0f, -1.0f,
    0.0f,  0.0f, -1.0f,
    0.0f,  0.0f, -1.0f,
    0.0f,  0.0f, -1.0f,

    0.0f,  0.0f, 1.0f,
    0.0f,  0.0f, 1.0f,
    0.0f,  0.0f, 1.0f,
    0.0f,  0.0f, 1.0f,
    0.0f,  0.0f, 1.0f,
    0.0f,  0.0f, 1.0f,

   -1.0f,  0.0f,  0.0f,
   -1.0f,  0.0f,  0.0f,
   -1.0f,  0.0f,  0.0f,
   -1.0f,  0.0f,  0.0f,
   -1.0f,  0.0f,  0.0f,
   -1.0f,  0.0f,  0.0f,

    1.0f,  0.0f,  0.0f,
    1.0f,  0.0f,  0.0f,
    1.0f,  0.0f,  0.0f,
    1.0f,  0.0f,  0.0f,
    1.0f,  0.0f,  0.0f,
    1.0f,  0.0f,  0.0f,

    0.0f, -1.0f,  0.0f,
    0.0f, -1.0f,  0.0f,
    0.0f, -1.0f,  0.0f,
    0.0f, -1.0f,  0.0f,
    0.0f, -1.0f,  0.0f,
    0.0f, -1.0f,  0.0f,

    0.0f,  1.0f,  0.0f,
    0.0f,  1.0f,  0.0f,
    0.0f,  1.0f,  0.0f,
    0.0f,  1.0f,  0.0f,
    0.0f,  1.0f,  0.0f,
    0.0f,  1.0f,  0.0f
};

float wall_1[] = {
    // 第一个三角形
    1.0f, 1.0f, 0.0f,
    1.0f, -1.0f, 0.0f,
    -1.0f, 1.0f, 0.0f,
    // 第二个三角形
    1.0f, -1.0f, 0.0f,
    -1.0f, -1.0f, 0.0f,
    -1.0f, 1.0f, 0.0f
};
float wall_2[] = {
     1.0f, 0.0f, 0.0f,
     0.0f, 1.0f, 0.0f,
     0.0f, 0.0f, 1.0f,

     0.0f, 1.0f, 0.0f,
     1.0f, 1.0f, 0.0f,
     0.0f, 0.0f, 1.0f,
};
float wall_3[] = {
     1.0f,1.0f,
     1.0f,0.0f,
     0.0f,1.0f,

     1.0f,0.0f,
     0.0f,0.0f,
     0.0f,1.0f
};

float trians_1[] = {
     0.5f, -0.5f, 0.0f,
    -0.5f, -0.5f, 0.0f,
     0.0f,  0.5f, 0.0f
};
float trians_2[] = {
     1.0f, 0.0f, 0.0f,
     0.0f, 1.0f, 0.0f,
     0.0f, 0.0f, 1.0f
};
float trians_3[] = {
      1.0,0.0,
      0.0,0.0,
      0.5,1.0
};


PointfragData noar::cube_vers = { cube_1,sizeof(cube_1) / sizeof(cube_1[0]),3, sizeof(cube_1) };
PointfragData noar::cube_col = { cube_2,sizeof(cube_2) / sizeof(cube_2[0]),3 , sizeof(cube_2) };
PointfragData noar::cube_texh = { cube_3,sizeof(cube_3) / sizeof(cube_3[0]),2, sizeof(cube_3) };
PointfragData noar::cube_norvec = { cube_4,sizeof(cube_4) / sizeof(cube_4[0]),3, sizeof(cube_4) };

PointfragData noar::wall_vers = { wall_1,sizeof(wall_1) / sizeof(wall_1[0]),3 , sizeof(wall_1) };
PointfragData noar::wall_col = { wall_2,sizeof(wall_2) / sizeof(wall_2[0]),3 , sizeof(wall_2) };
PointfragData noar::wall_texh = { wall_3,sizeof(wall_3) / sizeof(wall_3[0]),2 , sizeof(wall_3) };

PointfragData noar::train_vers = { trians_1,sizeof(trians_1) / sizeof(trians_1[0]),3  , sizeof(trians_1) };
PointfragData noar::train_col = { trians_2,sizeof(trians_2) / sizeof(trians_2[0]),3  , sizeof(trians_2) };
PointfragData noar::train_texh = { trians_3,sizeof(trians_3) / sizeof(trians_3[0]),2  , sizeof(trians_3) };
void noar::noarTest()
{
    float* fa0 = new float[] {0.0, 1.0, 2.0, 0.0, 1.0, 2.0};       //6
    float* fa1 = new float[] {110.0, 111.0, 112.0, 110.0, 111.0, 112.0};     //6
    //delete[] fa0;
    //fa0 = fa1;
    printarray("fa0数据", fa0, 6);
    printarray("fa1数据", fa1, 6);
    PointfragData f0 = { fa0,6,2 };
    PointfragData f1 = { fa1,6,2 };

    float* attach = arraysum(fa0, fa1, 6, 6);
    float* attch2 = arrayTach(f0, f1);
    printarray("合并数组", attach, 12);
    printarray("穿插数组", attch2, 12);
    std::cout << "-----------------------------------------\n";
    PointfragData f01 = { cube_vers.data,cube_vers.size,cube_vers.classnum };
    PointfragData f02 = { cube_col.data,cube_col.size,cube_col.classnum };
    PointfragData f03 = { cube_texh.data,cube_texh.size,cube_texh.classnum };

    printarray("cube_vers", f01.data, f01.size);
    printarray("cube_col", f02.data, f02.size);
    printarray("cube_texh", f03.data, f03.size);

    float* atch0 = noar::arrayTach(f01, f02);
    PointfragData f04 = { atch0 ,f01.size + f02.size,f01.classnum + f02.classnum };
    float* atch1 = noar::arrayTach(f04, f03);

    delete[] atch0;
    delete[] fa0;
    delete[] fa1;

    printarray("最终大数组的合体", atch1, f04.size + f03.size);
    std::cout << "点的数量为 size/8 = " << (f04.size + f03.size) / 8;
}