#pragma once

#include "window.hpp"

class Game
{
public:
    Game();
    ~Game();

    void handleInput();
    void update();
    void render();
    Window* getWindow();

    void movePikachu();

private:
    void moveSprite();
    Window m_Window;
    sf::Sprite pikachuSprite;
    sf::Texture pickachuTexture;
};

