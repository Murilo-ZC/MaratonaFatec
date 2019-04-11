#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main()
{
    float n1, n2, res;
    cin >> n1;
    cin >> n2;
    res = n1 + n2;
    cout << setprecision(2) << res << endl;
    printf("%.2f\n", res);
    return 0;
}
