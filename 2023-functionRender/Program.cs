using System;

namespace 函数渲染器
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BufferWidth = 1000;
            string turnToString(double 函数渲染器)
            {
                //累加的方法 把字符拼接起来
                string form = "";
                int length = (int)函数渲染器;
                for (int i = 0; i < length; i++) form+="*";
                return form;  
            }
            //获取 该函数于 x坐标时的 对应的y值
            double sinx(float x)
            {//     7|sinx|
                
                return 20 * Math.Abs(Math.Sin(x)) + 4 * Math.Abs(Math.Cos(5*x));
            }

            double 函数值 = sinx(1000.0f);
            Console.WriteLine(函数值);
            string a = turnToString(函数值);   //2.6   ---> OO   5.5--->ooooo
            
            
            void printFunction(float a,float b,float step)
            {
                for (float i = a; i < b; i += step)
                {
                    函数值 = sinx(i);
                    string 渲染内容 = turnToString(函数值);
                    Console.WriteLine(渲染内容);
                }
            }
            printFunction(19.0f, 40.0f, 0.1f);
        }
       
        
    }
}
         
