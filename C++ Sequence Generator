#include <iostream>
using namespace std;

/*
 * Question:
 * Create a class A that takes an integer N as input and generates a sequence
 * of N numbers where each number alternates between 1 and 6. The program 
 * should start with 1 and then repeatedly switch from 1 and 6 for N iterations, 
 * displaying each number in the sequence separated by a space.
 * Use class and objects to solve the program.
 */

class A {
public:
    void generateSequence(int N) {
        for (int i = 0; i < N; i++)
            cout << (i % 2 == 0 ? 1 : 6) << " ";
        cout << endl;
    }
};

int main() {
    int N;
    cin >> N;
    
    A obj;
    obj.generateSequence(N);

    return 0;
}
