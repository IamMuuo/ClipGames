#include "game.hpp"

int main()
{
    Game game;

    while(!game.getWindow()->isDone())
    {
        game.update();
        game.render();
    }
    return 0;
}
