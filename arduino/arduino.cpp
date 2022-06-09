#include <iostream>

using namespace std;

/**
if you have any issue is probably for the line "system("clear");
change it according to your system"
**/

int main()
{
    system("clear");
    string command = "0";
    string lc_command = "0";
    string change_loop = "0";
    float number;

    while (true)
    {
        while (change_loop == "0")
        {
            cout << "usage:" << endl;
            cout << "l: move to left" << endl;
            cout << "r: move to right" << endl;
            cout << "c: move to center" << endl;
            cout << "a: activate time" << endl;
            cout << "x: quit" << endl;
            lc_command = command;
            cin >> command;
            system("clear");
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
                    cout << "moving to left" << endl;
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
                    cout << "moving to right" << endl;
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
                    cout << "moving to center" << endl;
                }
                else
                {
                    ;
                }
            }
            else if (command == "x")
            {
                system("clear");
                cout << "bye" << endl;
                break;
            }
            else if (command == "a")
            {
                cout << "input time (float): " << endl;
                cin >> number;
                change_loop = "1";
                system("clear");
            }
            else
            {
                cout << "invalid command" << endl;
            }
        }
        while (change_loop == "1")
        {
            cout << "usage (" << number << "ms):" << endl;
            cout << "l: move to left" << endl;
            cout << "r: move to right" << endl;
            cout << "c: move to center" << endl;
            cout << "a: deactivate time" << endl;
            cout << "x: quit" << endl;
            lc_command = command;
            cin >> command;
            system("clear");
            if (command == "l")
            {
                if (lc_command == "l")
                {
                    cout << "already left" << endl;
                }
                else if (lc_command == "r")
                {
                    cout << "moving to center (" << number << "ms)" << endl;
                    cout << "moving to left (" << number << "ms)" << endl;
                }
                else if (lc_command == "c")
                {
                    cout << "moving to left (" << number << "ms)" << endl;
                }
                else if (lc_command == "0")
                {
                    cout << "moving to left (" << number << "ms)" << endl;
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
                    cout << "moving to center (" << number << "ms)" << endl;
                    cout << "moving to right (" << number << "ms)" << endl;
                }
                else if (lc_command == "r")
                {
                    cout << "already right" << endl;
                }
                else if (lc_command == "c")
                {
                    cout << "moving to right (" << number << "ms)" << endl;
                }
                else if (lc_command == "0")
                {
                    cout << "moving to right" << endl;
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
                    cout << "moving to center (" << number << "ms)" << endl;
                }
                else if (lc_command == "r")
                {
                    cout << "moving to center (" << number << "ms)" << endl;
                }
                else if (lc_command == "c")
                {
                    cout << "already center" << endl;
                }
                else if (lc_command == "0")
                {
                    cout << "moving to center" << endl;
                }
                else
                {
                    ;
                }
            }
            else if (command == "x")
            {
                system("clear");
                cout << "bye" << endl;
                break;
            }
            else if (command == "a")
            {
                change_loop = "0";
            }
            else
            {
                cout << "invalid command" << endl;
            }
        }
    }
    return 0;
}