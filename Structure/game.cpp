#include "game.hpp"

Game::Game()
    : m_Window("Alive Improved!", sf::Vector2i(800, 600))
{
    // set up class member data

    pickachuTexture.loadFromFile("Images/player.png");

    pikachuSprite.setTexture(pickachuTexture);
    pikachuSprite.setScale(0.7,0.7);
}

Game::~Game(){}

void Game::update()
{
    m_Window.update();
    movePikachu();
}

void Game::movePikachu()
{
    ;
}

void Game::render()
{
    m_Window.BeginDraw();
    m_Window.Draw(pikachuSprite);
    m_Window.EndDraw();
}

Window* Game::getWindow()
{
    return &m_Window;
}
