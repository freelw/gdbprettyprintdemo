
#include <assert.h>
#include <map>
#include <string>
#include <vector>

struct dawang_demo
{
    int a;
};


void f1() {
    dawang_demo b;
    b.a = 222;
    assert(0);
}

void f2() {
    f1();
}

void f3() {
    f2();
}

int main() {
    f3();
    return 0;
}