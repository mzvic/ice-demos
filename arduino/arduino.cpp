#include <iostream>

using namespace std;

int main()
{
    string command = "0";
    string lc_command = "0";
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
                if (lc_command == "l")
                {
                    cout << "already left" << endl;
                }
                else if (lc_command == "r")
                {
                    cout << "moving to center" << endl;
                    cout << "moving to left" << endl;
                }
                else if (lc_command == "c")
                {
                    cout << "moving to left" << endl;
                }
                else if (lc_command == "0")
                {
                    ;
                }
                else
                {
                    ;
                }
            }
            else if (command == "r")
            {
                if (lc_command == "l")
                {
                    cout << "moving to center" << endl;
                    cout << "moving to right" << endl;
                }
                else if (lc_command == "r")
                {
                    cout << "already right" << endl;
                }
                else if (lc_command == "c")
                {
                    cout << "moving to right" << endl;
                }
                else if (lc_command == "0")
                {
                    ;
                }
                else
                {
                    ;
                }
            }
            else if (command == "c")
            {
                if (lc_command == "l")
                {
                    cout << "moving to center" << endl;
                }
                else if (lc_command == "r")
                {
                    cout << "moving to center" << endl;
                }
                else if (lc_command == "c")
                {
                    cout << "already center" << endl;
                }
                else if (lc_command == "0")
                {
                    ;
                }
                else
                {
                    ;
                }
            }

            else if (command == "x")
            {
                cout << "quit" << endl;
                break;
            }
            else if (command == "a")
            {
                cout << "input time (float): " << endl;
                cin >> number;
                cout << "you are dumb in  " << number << " dimensions" << endl;
            }
            else
            {
                cout << "invalid command" << endl;
            }
        }

        return 0;
    }
}