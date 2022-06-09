#pragma once

module Demo
{
    interface arduinointerface
    {
        void left(); 
        void center();
        void right();
        void leftwithtime(float time);
        void centerwithtime(float time);
        void rightwithtime(float time);
        void stop();
    }
}