#include <iostream>
#include <cmath>

using namespace std;

int MaiorAB(int a, int b){
    //return (a+b+abs(a-b))/2;
    int modulo = (a-b) < 0 ? (-1) * (a-b) : (a-b);
    return (a+b+modulo) / 2;
}

int main()
{
    int a,b,c;
    cin >> a >> b >> c;
    int maior = MaiorAB(a,b);
    maior = MaiorAB(maior, c);
    cout << maior << " eh o maior" << endl;
    return 0;
}
