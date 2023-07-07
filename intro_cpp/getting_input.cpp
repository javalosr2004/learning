#include <iostream>
#include <string>
#include <format>

std::string getUserInput(std::string text){
    std::cout << text;
    std::string temp;
    std::cin >> temp;
    return temp;
}

int main(){
    std::string name = getUserInput("What is your name: ");
    std::cout << "\nThe length of your name is " << name.length() << std::endl;
    return 0;
}