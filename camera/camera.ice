#pragma once

module Demo
{
    interface video
    {
        idempotent void takephoto(); //Guiones bajos no funcionan nombrando a la función. "illegal underscore in identifier 'take_photo'"

        void shutdown();
    }
}