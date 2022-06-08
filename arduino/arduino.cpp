#include <iostream>

using namespace std;

int main()
{
    string command;
    float number;
    while (true)
    {
        while (command != "a")
        {
            cout << "usage:" << endl;
            cout << "l: move to left" << endl;
            cout << "r: move to right" << endl;
            cout << "c: move to center" << endl;
            cout << "a: activate time" << endl;
            cout << "x: quit" << endl;
            cin >> command;
            if (command == "l")
            {
                cout << "move to left" << endl;
            }
            else if (command == "r")
            {
                cout << "move to right" << endl;
            }
            else if (command == "c")
            {
                cout << "move to center" << endl;
            }

            else if (command == "x")
            {
                cout << "quit" << endl;
                break;
            }
            else if (command == "a")
            {
                ;
            }
            else
            {
                cout << "invalid command" << endl;
            }
        }

        cout << "input time (float): " << endl;
        cin >> number;
        cout << "usage:" << endl;
        cout << "l: move to left" << endl;
        cout << "r: move to right" << endl;
        cout << "c: move to center" << endl;
        cout << "a: deactive time" << endl;
        cout << "x: quit" << endl;
        cin >> command;
        if (command == "l")
        {
            cout << "move to left with " << number << "ms." << endl;
        }
        else if (command == "r")
        {
            cout << "move to right" << number << "ms." << endl;
        }
        else if (command == "c")
        {
            cout << "move to center" << number << "ms." << endl;
        }

        else if (command == "x")
        {
            cout << "quit" << endl;
            break;
        }
        else if (command == "a")
        {
            ;
        }
        else
        {
            cout << "invalid command" << endl;
        }
    }

    return 0;
}