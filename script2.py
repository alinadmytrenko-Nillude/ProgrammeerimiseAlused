#include <iostream>
using namespace std;
class Shape {
public:
    virtual void draw() { // Виртуальная функция
        cout << "Drawing a shape" << endl;
    }
};
class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a circle" << endl;
    }
};
int main() {
    Shape* shape = new Circle();
    shape->draw(); // Drawing a circle
    delete shape;
    return 0;
}