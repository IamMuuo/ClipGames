#include "game.hpp"
#include "window.hpp"

Game::Game()
    : m_Window("Alive Improved!", sf::Vector2i(800, 600))
{
    // set up class member data

    pickachuTexture.loadFromFile("Image/player.png");

    pikachuSprite.setTexture(pickachuTexture);
    pikachuSprite.setScale(0.25,0.25);
    pikachuSprite.setOrigin(pickachuTexture.getSize().x / 2, pickachuTexture.getSize().y / 2);
   pikachuSprite.setPosition(400, 300);
}

Game::~Game(){}

void Game::update()
{
    m_Window.update();
    movePikachu();
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

void Game::movePikachu()
{
    if (pikachuSprite.getPosition().x < m_Window.getWindowSize().x)
        pikachuSprite.setPosition(pikachuSprite.getPosition().x + 10,pikachuSprite.getPosition().y);
    else
        pikachuSprite.setPosition(pikachuSprite.getPosition().x - 10,pikachuSprite.getPosition().y);
}
